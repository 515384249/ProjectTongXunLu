# -*- coding: utf-8 -*-
# coding:utf-8


import xlrd  # excel读工具
import jieba.posseg


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

