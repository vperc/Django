from django.db import models

class Grades(models.Model):
                                                          #字段
    gname = models.CharField(max_length=20)               #班级名称
    gdate = models.DateTimeField()                        #成立时间
    ggirlnum = models.IntegerField()                      #女生总数
    gboyname = models.IntegerField()                      #男生总数
    isDelete = models.BooleanField(default=False)         #是否删除

class Students(models.Model):
    sname = models.CharField(max_length=20)               #姓名
    sgender = models.BooleanField(default=True)           #性别
    sage = models.IntegerField()                          #年龄
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #关联外键
    sgrade = models.ForeignKey("Grades")