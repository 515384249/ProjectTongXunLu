def celldatajiegou(data):
    data_len = len(data)
    zimu_sum = 0
    shuzi_sum = 0
    hanzi_sum = 0
    other_sum = 0
    type = {
        "hanzi":zimu_sum,
        "shuzi":shuzi_sum,
        "zimu":zimu_sum,

    }
    for strs in data:
        # 如果在字符串中有字符，那么字符的数量+1
        if strs.isalpha():
            if strs >= u'\u4e00' and u'\u9fa5' >= strs:
                hanzi_sum += 1
            else:
                zimu_sum += 1
        # 如果在字符串中有数字，那么数字的数量+1
        elif strs.isdigit():
            shuzi_sum += 1
        # 如果在字符串中有特殊字符那么特殊字符的数量+1
        else:
            other_sum += 1
    type["hanzi"] = hanzi_sum
    type["zimu"] = zimu_sum
    type["shuzi"] = shuzi_sum
    return type
    # print("该字符changdu：%d" % data_len)
    # print("该字符串中的hanzi有：%d" % hanzi_sum)
    # print("该字符串中的zimu有：%d" % zimu_sum)
    # print("该字符串中的shuzi有：%d" % shuzi_sum)
    # print("该字符串中的字符有：%d" % other_sum)


def th_type(data):
    dict_list = ["姓名", "邮箱", "办公", "电话"]

    if data.find("姓名") >= 0:
        type = "xingming_th"
    elif data.find("邮箱")>= 0 or data.find("mail")>= 0:
        type = "youxiang_th"
    elif data.find("电话") >= 0:
        type = "dianhua_th"
    elif data.find("办公")>= 0:
        type = "dizhi_th"
    else:
        type ="th"
    return type

def td_type(data):
    td_type = 'qita'
    type = dict()
    type = celldatajiegou(data)
    if type["shuzi"]>=4 and type["hanzi"] == 0 and type["zimu"] == 0:
        td_type = 'dianhua'
    if type["shuzi"]>0 and (type["hanzi"] > 0 or type["zimu"] > 0):
        td_type = 'dizhi'
    if  type["shuzi"]==0 and type["hanzi"] > 1 and type["zimu"] == 0 and  type["hanzi"] < 4:
        td_type = 'xingming'
    return  td_type






#
#
# def shujujiexi(sheet_index,table_name,):
#     db_dict =  dict();
#
# db_list = ["id","yuanx","xi","xingming","zhiwu","dizhi","youxiang"]
# dict_list = ["姓名","邮箱","办公","电话"]
#     # table 逐行與list對比，
#     for i in range(0, nrows):
#         row = table.row_values(i)  # 获取每行值
#         for j in range(0, ncols):
#              row[j]
#         if row:  # 查看行值是否为空
