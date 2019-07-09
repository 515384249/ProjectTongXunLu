import json
import os
from django.shortcuts import reverse, redirect
from . import models
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.db.models import Q
from django.http import FileResponse
from tools import excel
from django.conf import settings



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
        # if search:  # 判断是否有搜索字
        #     all_records = models.tongxunlu.objects.filter(
        #         Q(xingming__contains=search) | Q(yuan__contains=search) | Q(xi__contains=search) | Q(
        #             zhuanye__contains=search) | Q(zhiwu__contains=search) | Q(dianhua__contains=search) | Q(
        #             dizhi__contains=search)
        #     ).values('id', 'yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu', 'dianhua', 'dizhi').order_by('id')
        # else:
        #     all_records = models.tongxunlu.objects.all().values('id', 'yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu',
        #                                                         'dianhua',
        #                                                         'dizhi')
        if search:  # 判断是否有搜索字
            all_records = models.people_infor.objects.filter(
                Q(xingming__contains=search) | Q(dwmc__contains=search) | Q(ksmc__contains=search)
                 | Q(dianhua__contains=search) | Q(dizhi__contains=search)
            ).values('id', 'dwmc', 'ksmc', 'xingming',  'dianhua', 'dizhi','dwh').order_by('dwh')

        else:
            all_records = models.people_infor.objects.all().values('id', 'dwmc', 'ksmc', 'xingming',  'dianhua', 'dizhi').order_by('id')
        ppp = json.dumps(list(all_records))
        return HttpResponse(ppp)
    elif request.method == "POST":
        search = request.POST.get('search')  # how many items per page
        print("post search index is %s" % search)
        # if search:  # 判断是否有搜索字
        #     all_records = models.tongxunlu.objects.filter(
        #         Q(xingming__contains=search) | Q(yuan__contains=search) | Q(xi__contains=search) | Q(
        #             zhuanye__contains=search) | Q(zhiwu__contains=search) | Q(dianhua__contains=search) | Q(
        #             dizhi__contains=search)
        #     ).values('id', 'yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu', 'dianhua', 'dizhi').order_by('id')
        # else:
        #     all_records = models.tongxunlu.objects.all().values('id', 'yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu',
        #                                                         'dianhua',
        #                                                         'dizhi')
        if search:  # 判断是否有搜索字
            all_records = models.people_infor.objects.filter(
                Q(xingming__contains=search) | Q(dwmc__contains=search) | Q(ksmc__contains=search)
                 | Q(dianhua__contains=search) | Q(dizhi__contains=search)
            ).values('id', 'dwmc', 'ksmc', 'xingming',  'dianhua', 'dizhi','dwh').order_by('dwh')

        else:
            all_records = models.people_infor.objects.all().values('id', 'dwmc', 'ksmc', 'xingming',  'dianhua', 'dizhi').order_by('id')
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
    return render(request, 'mylogin.html', context)
def glydl(request):
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
        context = {"case_name": yuan}
    return render(request, 'guanliyuan.html', context)


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

