from django.db import models

# Create your models here.
class Brand
{
    brandId = IntField(required=True);
    brandName=StringField(required=True);
    brandsCates=ListField();
    brandsStarProduct=ListField();
    brandsAge=DictField();
    brandsSerial=DictField();
}

class Product
{
    ProductId = IntField(required=True);
    ProductName = StringField(required=True);
    ProductCategory = IntField();
    ProductAge = DictField();
    ProductGongxiao = ListField();
    ProductPLScore=FloatField();
    ProductJieshao = String();
    ProductFangfa=String();
}

class category
{
    categoryId= IntField(required=True);
    categoryName= StringField(required=True);
    categoryProducts=ListField();
}

