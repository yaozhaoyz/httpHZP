from django.db import models
from mongoengine import *
from hzp.settings import DBNAME
from django import forms
from django.forms.widgets import *
from django.http import HttpResponse

connect(DBNAME)

# Create your models here.
class C_Brand(Document):
    brandId = IntField(required=True);
    brandName=StringField(required=True);
    brandsCates=ListField();
    brandsStarProduct=ListField();
    brandsProductItems=ListField();# stroe the product id.
    brandsAge=DictField();
    brandsSerial=DictField();

class C_Product(Document):
    ProductId = IntField(required=True);
    ProductName = StringField(required=True);
    ProductCategory = StringField(required=True)
    ProductAge = DictField(); # five period
    ProductGongxiao = ListField();
    ProductPLScore = FloatField();
    ProductJieshao = StringField();
    ProductUsage=StringField();
    ProductImgURL = StringField();

class C_Category(Document):
    categoryId= IntField(required=True);
    categoryName= StringField(required=True);
    categoryProducts=ListField();

