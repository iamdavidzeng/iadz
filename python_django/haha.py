from django.db import models


class Country(models.Model):
    code = models.CharField('国家代码', max_length=8)
    name = models.CharField('名称', max_length=16)
    name_native = models.CharField('全称', max_length=24)


class City(models.Model):
    country = models.ForeignKey(Country)
    code = models.CharField('城市代码', max_length=16)
    name = models.CharField('城市名称', max_length=16)


class Company(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField('公司名', max_length=32)
    address = models.CharField('公司地址', max_length=64)


# 然后就是对于查询的使用了
# 找出一个城市中的所有公司对象有两种方式
# 1
queryset = Company.objects.filter(city_id=1)
# 2
city = City.objects.get(id=1)
queryset = city.comapny_set.all()

# 查询一个国家的所有公司，直接通过公司查询不了
# 这个时候就可以使用到Django的关联查询了
queryset = Comapny.objects.filter(city__country__id=1)