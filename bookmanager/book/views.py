from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('index')


# #########################新增数据###########################################
from book.models import BookInfo, PeopleInfo
#
# # 方式一
# book = BookInfo(
#     name='Django',
#     pub_date='2000-1-1',
#     readcount=10
# )
#
# # 方式二
# BookInfo.objects.create(name='测试开发入门',
#                         pub_date='2000-1-1',
#                         readcount=100)
#
# BookInfo.objects.get(id=6)
#
# #########################修改数据###########################################
# # 方式一
# book = BookInfo.objects.get(id=6)
# book.name = '运维入门'
# book.save()
# # 方式二
# BookInfo.objects.filter(id=5).update(name='Flask', commentcount=666)
#
# book.delete()
#
# #########################查询数据###########################################
#
# books = BookInfo.objects.all()
#
# book = BookInfo.objects.filter(id__exact=2)
#
# books = BookInfo.objects.filter(name__contains='湖')
#
# books = BookInfo.objects.filter(name__endswith='部')
#
# BookInfo.objects.filter(name__isnull=False)
#
# BookInfo.objects.filter(id__in=(1, 3, 5))
#
# #  gt great  >
# BookInfo.objects.filter(id__gt=2)
#
# #  lt little  <
# BookInfo.objects.filter(id__lt=2)
#
# #  gte great equal >=
# BookInfo.objects.filter(id__gte=2)
#
# BookInfo.objects.exclude(id=3)
#
# BookInfo.objects.filter(pub_date__year=1980)
#
# BookInfo.objects.filter(pub_date__gt='1985-1-1')
#
# BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
#
# BookInfo.objects.filter(readcount__gte=20, id__lte=3)
#
# from django.db.models import Q
#
# BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))
#
# ###############################聚合函数###############################
from django.db.models import Sum, Max, Min, Count, Avg
#
# BookInfo.objects.aggregate(Sum('readcount'))
# BookInfo.objects.aggregate(Max('commentcount'))
#
# BookInfo.objects.all().order_by('commentcount')
# BookInfo.objects.all().order_by('-commentcount')
#
#
# ###############################级联查询###############################
# book = BookInfo.objects.get(id=1)
# book.peopleinfo_set.all()
# # people = PeopleInfo.objects.get(id=1)
# # people.book
# BookInfo.objects.filter(peopleinfo__name='郭靖')
#
# BookInfo.objects.filter(peopleinfo__description__contains='八')
#
#
# PeopleInfo.objects.filter(book__name='天龙八部')
#
# PeopleInfo.objects.filter(book__readcount__gt=30)
# from django.core.paginator import Paginator
#
# persons = PeopleInfo.objects.all()
# l = [per.name for per in persons]
# p = Paginator(l, 2)
