from django.db import models
from mongoengine import *
from hzp.settings import DBNAME
from django import forms
from django.forms.widgets import *
from django.http import HttpResponse

connect(DBNAME)
class Pid(Document):
    pid = IntField(required=True)

# Create your models here.
class C_Brand(Document):
    brandId = IntField();
    brandName=StringField(required=True);
    brandsCates=ListField();
    brandsStarProduct=ListField();
    brandsProductItems=ListField();# stroe the product id.
    brandsAge=DictField();# statistic five period
    brandsSerial=DictField();
    brandPlace = StringField();
    brandBirthday = StringField();
    brandGuanwang = StringField();
    brandImg = StringField();
    brandJieshao = StringField();

class C_Product(Document):
    ProductId = IntField();
    ProductName = StringField(required=True);
    ProductPrice = StringField();
    ProductCategory = StringField()
    ProductBrand = StringField()
    ProductAge = DictField(); # five period
    ProductGongxiao = ListField();
    ProductScore = StringField(); # 
    ProductPLScore = FloatField();
    ProductJieshao = StringField();
    ProductSkin = ListField();
    ProductUsage=StringField();
    ProductImgURL = StringField();
    ProductLinkURL= StringField();
    ProductDaPei = StringField();

class C_Category(Document):
    categoryId= IntField(required=True);
    categoryName= StringField(required=True);
    categoryProducts=ListField();

