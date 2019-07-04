import json
import os
from django.shortcuts import reverse, redirect
from . import models
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.db.models import Q
from django.http import FileResponse
from tools import excel
from django.conf import settings

# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt


def download(request):
    file = open('static/xlsx/模板.xlsx', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="xlsx_file.xlsx"'
    return response


def fileupload(request):
    context = {}

    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join(settings.MEDIA_ROOT, myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        # 解析xlxs把数据存入数据库
        tablelist = []
        rows_list = []
        rows_list1 = []
        tablelist = excel.get_tables(os.path.join(settings.MEDIA_ROOT, myFile.name))
        # 获得所有电话
        cell = dict()
        cells = []
        # for i in tablelist:
        #     rows_list1 = excel.get_table_rows(i)
        #     rows_list.extend(rows_list1)
        #     for j in range(0, len(rows_list)):
        #         if rows_list[j][0]:
        #             cell["yuan"] = rows_list[j][0]
        #         elif "yuan" in cell:
        #             del cell["yuan"]
        #         if rows_list[j][1]:
        #             cell["xi"] = rows_list[j][1]
        #         elif "xi" in cell:
        #             del cell["xi"]
        #         if rows_list[j][2]:
        #             cell["zhuanye"] = rows_list[j][2]
        #         elif "zhuanye" in cell:
        #             del cell["zhuanye"]
        #         if rows_list[j][3]:
        #             cell["xingming"] = rows_list[j][3]
        #         elif "xingming" in cell:
        #             del cell["xingming"]
        #         if rows_list[j][4]:
        #             cell["zhiwu"] = rows_list[j][4]
        #         elif "zhiwu" in cell:
        #             del cell["zhiwu"]
        #         if rows_list[j][5]:
        #             cell["dianhua"] = rows_list[j][5]
        #         elif "dianhua" in cell:
        #             del cell["dianhua"]
        #         if rows_list[j]:
        #             cell["dizhi"] = rows_list[j][6]
        #         elif "dizhi" in cell:
        #             del cell["dizhi"]
        #         if rows_list[j][7]:
        #             cell["youxiang"] = rows_list[j][7]
        #         elif "youxiang" in cell:
        #             del cell["youxiang"]
        for i in tablelist:
            rows_list1 = excel.get_table_rows(i)
            rows_list.extend(rows_list1)
            for j in range(0, len(rows_list)):
                num = len(rows_list[j])
            if num > 0:
                cell["yuan"] = rows_list[j][0]
            elif "yuan" in cell:
                del cell["yuan"]
            if num > 1:
                cell["xi"] = rows_list[j][1]
            elif "xi" in cell:
                del cell["xi"]
            if num > 2:
                cell["zhuanye"] = rows_list[j][2]
            elif "zhuanye" in cell:
                del cell["zhuanye"]
            if num > 3:
                cell["xingming"] = rows_list[j][3]
            elif "xingming" in cell:
                del cell["xingming"]
            if num > 4:
                cell["zhiwu"] = rows_list[j][4]
            elif "zhiwu" in cell:
                del cell["zhiwu"]
            if num > 5:
                cell["dianhua"] = rows_list[j][5]
            elif "dianhua" in cell:
                del cell["dianhua"]
            if num > 6:
                cell["dizhi"] = rows_list[j][6]
            elif "dizhi" in cell:
                del cell["dizhi"]
            if num > 7:
                cell["youxiang"] = rows_list[j][7]
            elif "youxiang" in cell:
                del cell["youxiang"]
                try:
                    models.tongxunlu.objects.create(**cell)
                except:
                    return HttpResponse("excel文件格式不正确!")
                models.tongxunlu.objects.filter(zhuanye="专业").delete()
                models.tongxunlu.objects.filter(yuan="院/单位").delete()
    context = {
        "data": "保存成功",
    }

    return render(request, 'ceshi.html', context)


def showtable(request):
    if request.method == "GET":
        search = request.GET.get('search')  # how many items per page
        print("search index is %s"%search)
        if search:  # 判断是否有搜索字
            all_records = models.tongxunlu.objects.filter(
                Q(xingming__contains=search) | Q(yuan__contains=search) | Q(xi__contains=search) | Q(
                    zhuanye__contains=search) | Q(zhiwu__contains=search) | Q(dianhua__contains=search) | Q(
                    dizhi__contains=search)
            ).values('id', 'yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu', 'dianhua', 'dizhi').order_by('id')
        else:
            all_records = models.tongxunlu.objects.all().values('id', 'yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu',
                                                                'dianhua',
                                                                'dizhi')
        ppp = json.dumps(list(all_records))
        return HttpResponse(ppp)
    elif request.method == "POST":
        search = request.POST.get('search')  # how many items per page
        print("post search index is %s" % search)
        if search:  # 判断是否有搜索字
            all_records = models.tongxunlu.objects.filter(
                Q(xingming__contains=search) | Q(yuan__contains=search) | Q(xi__contains=search) | Q(
                    zhuanye__contains=search) | Q(zhiwu__contains=search) | Q(dianhua__contains=search) | Q(
                    dizhi__contains=search)
            ).values('id', 'yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu', 'dianhua', 'dizhi').order_by('id')
        else:
            all_records = models.tongxunlu.objects.all().values('id', 'yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu',
                                                                'dianhua',
                                                                'dizhi')
        ppp = json.dumps(list(all_records))
        print(ppp)
        return HttpResponse(ppp)
    else:
        return HttpResponse("eeee")

# @login_required
# @require_GET
def ceshi(request):
    context = {}
    return render(request, 'ceshi.html', context)


@login_required
@require_GET
def mylogout(request):
    print("logout")
    try:
        logout(request)
    except:
        pass
    return render(request, 'mylogin.html')


def mylogin(request):
    context = {}
    if request.method == 'POST':
        print("post")
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        print(username)
        print(pwd)
        user = authenticate(request, username=username, password=pwd)
        if user:
            login(request, user)
            return redirect(reverse('ceshi'))
        else:
            return HttpResponse("<h1>密码错误</h1>")
    elif request.method == 'GET':
        yuan = models.yuan.objects.all().values('name')
        context = {"case_name":yuan}
        return render(request, 'mylogin.html', context)


def kjfs_search(request):
    if request.method == 'POST':
        print("收到post")
        type = request.POST.get('type')  # 测试是否能够接收到前端发来的name字段
        print(type)
        a = request.POST.get('data')  # 测试是否能够接收到前端发来的name字段
        b = a.strip(" ")
        if (type == "kjjs"):
            data = models.tongxunlu.objects.filter(yuan__contains=b).values('id', 'yuan', 'xi', 'zhuanye', 'xingming',
                                                                            'zhiwu',
                                                                            'dianhua', 'dizhi')

            json_data = json.dumps(list(data))

            return HttpResponse(json_data)
    else:
        return HttpResponse("<h1>test</h1>")


def kjfs_edit(request):
    if request.method == 'POST':

        type = request.POST.get('type')  # 测试是否能够接收到前端发来的name字段
        a = request.POST.get('data')  # 测试是否能够接收到前端发来的name字段
        print("this is save %s" % a)
        c = json.loads(a)
        if (type == 'save'):

            for i in c:
                if ("id" in i):
                    if  (i["id"]=='-'):
                        del i['state']
                        del i['id']
                        models.tongxunlu.objects.create(**i)
                    else:

                        if (models.tongxunlu.objects.filter(id=i["id"]).exists()):
                            print("updata")

                            b = i['id']
                            del i['id']
                            del i['state']
                            models.tongxunlu.objects.filter(id=b).update(**i)

                else:
                    print("new")
                    del i['state']
                    models.tongxunlu.objects.create(**i)

        elif (type == 'del'):
            for i in c:
                models.tongxunlu.objects.filter(id=i['id']).delete()

        return HttpResponse("success")
    else:
        return HttpResponse("<h1>test</h1>")


def cdh(request):
    context = {}
    if request.method == 'GET':
        case_name = request.GET.get('name')
        case_page = request.GET.get('page')
    elif request.method == 'POST':
        case_name = request.POST.get('name')
        case_page = request.POST.get('page')
    if case_name:
        contact_list = models.tongxunlu.objects.filter(
            Q(xingming__contains=case_name) | Q(yuan__contains=case_name) | Q(xi__contains=case_name) | Q(
                zhuanye__contains=case_name) | Q(zhiwu__contains=case_name) | Q(dianhua__contains=case_name) | Q(
                dizhi__contains=case_name)
        ).values('yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu', 'dianhua', 'dizhi').order_by('id')
    else:
        contact_list = models.tongxunlu.objects.all().values('yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu', 'dianhua',
                                                             'dizhi').order_by('id')

    paginator = Paginator(contact_list, 2200)  # 每页显示25条
    yuanxi = models.yuan.objects.all().values('name', 'father_name')
    try:
        contacts = paginator.page(case_page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数，返回第一页。
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(1)
    context = {'contacts': contacts,
               'case_name': yuanxi,
               'search_name': case_name,
               }
    return render(request, 'mylogin.html', context)
