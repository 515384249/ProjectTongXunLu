
# 1先找电话，根据电话建立 onedata实体， 赋值dianhua，
# 2  实体  前几列是否有电话
# 3 没有的话，找前几列的cell，匹配对应的type
# 4  有的话  找前一个电话 <olnum <self.colnum 的cell ,匹配对应的 type
# 5  给 属性赋值
# 6  将实体写入数据库
#
