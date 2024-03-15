from django.db import models


# Create your models here.

class Bookinfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍管理'


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.IntegerField()
    description = models.CharField()
    is_delete = models.BooleanField()
    book_id = models.ForeignKey(Bookinfo, True)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '角色管理'
