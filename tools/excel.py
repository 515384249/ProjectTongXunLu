# -*- coding: utf-8 -*-
# coding:utf-8


import xlrd  # excel读工具
import jieba.posseg

datalist = []
kk = 0
wb = xlrd.open_workbook("E:\北京交通大学办公室号码表(1).xlsx")  # 打开文件  這個文件名要根據傳過來的值確定
sheets = wb.sheet_names()
tablelist = []
rows_list = []


def get_tables(filmpath):
    tablelist = []
    wb = xlrd.open_workbook(filmpath)
    sheets = wb.sheet_names()
    for i in range(len(sheets)):  # 有几个sheet
        table = wb.sheet_by_index(i)
        tablelist.append(table)
    return tablelist


def get_table_rows(table):
    row_value = []
    nrows = table.nrows  # 行数
    ncols = table.ncols
    for i in range(0, nrows):
        row = table.row_values(i)  # 获取每行值
        for j in range(0, ncols):
            if type(row[j]) == float:
                row[j] = int(row[j])
                row[j] = str(row[j])
        row_value.append(row)
    return row_value


def get_dianhuan(row, datalist):
    for i in row:
        if bijiao.td_type(i) == 'dianhua':
            datalist.append({"dianhua": i})


def search_name(datalist, row):
    pass

#
# # tablelist = get_tables("E:\北京交通大学办公室号码表(1).xlsx")
# tablelist = get_tables("E:\手动编辑.xlsx")
# # 获得所有电话
# for i in tablelist:
#     rows_list1 = get_table_rows(i)
#     rows_list.extend(rows_list1)
#     for j in rows_list1:
#         get_dianhuan(j, datalist)
# print(len(datalist))
# print(len(rows_list))
# # 为所有cell打标签  realtype
# cell_type_list = []
# # 获得
# for j in range(0, len(rows_list)):
#     for i in range(0, len(rows_list[j])):
#         a = bijiao.td_type(rows_list[j][i])
#         b = bijiao.th_type(rows_list[j][i])
#         cell_type_list.append({"row_num": j, "col_num": i, "td_type": a, "th_type": b, "value": rows_list[j][i]})
# print(len(cell_type_list))
# for k in range(0, len(cell_type_list)):
#
#     if cell_type_list[k]["td_type"] == "xingming":
# #     看这个是不是姓名
#
#         colnum = cell_type_list[k]["col_num"]
#         rownum  = cell_type_list[k]["row_num"]
#         for i in range(0, k):
#             if cell_type_list[i]["col_num"] == colnum:
#                 if (cell_type_list[i]["th_type"] == "xingming_th" and  cell_type_list[k]["th_type"] == "th"):
#                         cell_type_list[k]["td_type"] = 'realxingming'
#
# for k in range(0, len(cell_type_list)):
#
#     if  cell_type_list[k]["td_type"] =="realxingming":
#         jb4 = jieba.posseg.cut(cell_type_list[k]["value"])
#         for i in jb4:
#             if( i.flag == 'nr'):
#                 print(i.word + '-----' + i.flag)
#                 kk = kk+1
# print(kk)
#
#
# #
#jieba.load_userdict(file_name) # file_name为自定义词典的路径
# for i in range(len(sheets)):  # 有几个sheet
#     table = wb.sheet_by_index(i)
#     tablelist.append(table)
#     print(table.name)
#     nrows = table.nrows  # 行数
#     print(nrows)
#     ncols = table.ncols  # 列数
#     print("列數=%s" % ncols)
#     colnames = table.row_values(1)
#     print("列名字=%s" % colnames)
#     WorkList = []
#     cells = []
#     lines = []
#     realtype = ''
#     for i in range(0, nrows):
#         row = table.row_values(i)  # 获取每行值
#         for j in range(0, ncols):
#             if type(row[j]) == float:  # 如果值为float则转换为int,避免出现1输出为1.0的情况
#                 row[j] = int(row[j])
#                 row[j] = str(row[j])
#             thtype = bijiao.th_type(row[j])
#             tdtype = bijiao.td_type(row[j])
#             cell = CellJieGou()
#             cell.td_type = tdtype
#             cell.th_type = thtype
#             cell.row_num = i
#             cell.col_num = j
#             cell.sheet_name = table.name
#             k = i
#             if cell.td_type == 'dianhua':
#                 # while k < i:
#                 #     if table.cell(k, j).value == 'dianhua_th':
#                 #         realtype = 'dianhuahaoma'
#                 #         break
#                 #     k = k - 1
#                 # if realtype == 'dianhuahaoma':
#                 cell.read_type = 'dianhua'
#
#                 cells.append(cell)
