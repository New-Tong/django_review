from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('index')


#########################新增数据###########################################
from book.models import BookInfo

# 方式一
book = BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
)

# 方式二
BookInfo.objects.create(name='测试开发入门',
                        pub_date='2000-1-1',
                        readcount=100)

BookInfo.objects.get(id=6)

#########################修改数据###########################################
# 方式一
book = BookInfo.objects.get(id=6)
book.name = '运维入门'
book.save()
# 方式二
BookInfo.objects.filter(id=5).update(name='Flask', commentcount=666)

book.delete()

books = BookInfo.objects.all()

book=BookInfo.objects.filter(id__exact=2)