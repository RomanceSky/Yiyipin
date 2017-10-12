# -*- coding: utf-8 -*-

from django.http import HttpResponse

from User.models import Test

# 数据库操作

def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    test2 = Test(name='意艺品')
    test2.save()

    return HttpResponse("<p>数据添加成功!</p>")
