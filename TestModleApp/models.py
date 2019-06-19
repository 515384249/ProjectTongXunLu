from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

#建立用户表
class myuser(models.Model):
    usercode = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    deptname = models.CharField(max_length=30)  #
    deptcode = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    phonenum = models.CharField(max_length=30, null=True)
class myphone(models.Model):
    usercode = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    deptname = models.CharField(max_length=30)  #
    deptcode = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    phonenum = models.CharField(max_length=30, null=True)

#数据结构
#基础字段
#院      yuan
#系      xi
#专业&科室  zhuanye
#二级专业&二级科室   erjizhuanye
# 姓名    xingming
# 职务    zhiwu
# 职责    zhize
# 电话/传真 dianhua
# 邮箱          youxiang
# 办公地址    dizhi
class tongxunlu(models.Model):
    yuan = models.CharField(max_length=30)
    xi = models.CharField(max_length=30)
    zhuanye = models.CharField(max_length=30)
    erjizhuanye = models.CharField(max_length=30, null=True)
    xingming = models.CharField(max_length=30, null=True)
    zhiwu = models.CharField(max_length=30, null=True)
    zhize = models.CharField(max_length=500, null=True)
    dianhua = models.CharField(max_length=30, null=True)
    dizhi = models.CharField(max_length=30, null=True)
    youxiang = models.CharField(max_length=30, null=True)
#  系名称  院名称
class yuan(models.Model):
    name  =   models.CharField(max_length=30)
    has_son =  models.CharField(max_length=1, null=True)
    has_father = models.CharField(max_length=1, null=True)
    father_name = models.CharField(max_length=30, null=True)
    son_name = models.CharField(max_length=30, null=True)

