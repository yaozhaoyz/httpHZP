# coding=utf8
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from hzp.settings import URL_PREFIX 
from models import *
import urllib
import datetime
import os
import json

# Create your views here.
def test(request):
    responseAll = {}
    responseAll["test"]="hello world";
    return HttpResponse(json.dumps(responseAll), content_type="application/json")

def mainProcess(request):
    if(request.method == 'GET'):
        responseAll = {} 
        typeId = request.GET.get('typeId','');
        fromCard = request.GET.get('fromcard','');
        toCard = request.GET.get('tocard','');
        if(typeId == "")or (fromCard =="")or(toCard==""):
            responseAll["RetCode"] = "Ret_ERROR_TypeId_MISSING";
            return HttpResponse(json.dumps(responseAll), content_type="application/json")
        elif (typeId == "1"): #品牌主卡(L1Brand)的触发
            brand = request.GET.get("brand","");
            if(brand == ""):
                responseAll["RetCode"] = "Ret_ERROR_Brand";
                return HttpResponse(json.dumps(responseAll), content_type="application/json")
            else:
                brand = brand.encode("utf8")
                brand = urllib.quote( brand )
                aItem = {}
                aItem["StarProduct"] = str(URL_PREFIX)+"/hzp/main/?fromcard=L1Brand&tocard=L2Brand_StarProduct&typeId=2&brand="+brand;
                aItem["CategoryList"]= str(URL_PREFIX)+"/hzp/main/?fromcard=L1Brand&tocard=L2Brand_Category&typeId=3&brand="+brand;
                aItem["ClassicSerial"]= str(URL_PREFIX)+"/hzp/main/?fromcard=L1Brand&tocard=L2Brand_ClassicSerial&typeId=4&brand="+brand;
                aItem["SimilarProduct"]= str(URL_PREFIX)+ "/hzp/main/?fromcard=L1Brand&tocard=L2Brand_SimilarProduct&typeId=5"+brand;
                responseAll["Items"] = aItem 
                responseAll["RetCode"] = "Ret_OK";
            return HttpResponse(json.dumps(responseAll), content_type="application/json")
        elif (typeId == "2"): #品牌主卡(L1Brand) ->子卡(L2Brand_StarProduct) 
            brand = request.GET.get("brand","");
            if(brand == ""):
                responseAll["RetCode"] = "Ret_ERROR_Brand";
                return HttpResponse(json.dumps(responseAll), content_type="application/json")
            else:
                brand = brand.encode("utf8")
                brand = urllib.quote( brand )
                aItem = {}
                theBrand = C_Brand.objects.filter(brandName = brand)
                if((theBrand == None) or (len(theBrand) == 0)):
                    responseAll["RetCode"] = "Ret_ERROR_BrandNotFound";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                starProductList = theBrand[0].brandsStarProduct;
                if( len(starProductList)<=0 ):
                    responseAll["RetCode"] = "Ret_ERROR_NoneStarProduct";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                responseAll["Items"] = aItem 
                responseAll["RetCode"] = "Ret_OK";
            return HttpResponse(json.dumps(responseAll), content_type="application/json")
        elif (typeId == "3"): #品牌主卡(L1Brand) ->子卡(L2Brand_Category) 
            brand = request.GET.get("brand","");
            if(brand == ""):
                responseAll["RetCode"] = "Ret_ERROR_Brand";
                return HttpResponse(json.dumps(responseAll), content_type="application/json")
            else:
                brand = brand.encode("utf8")
                brand = urllib.quote( brand )
                aItem = {}
                theBrand = C_Brand.objects.filter(brandName = brand)
                if((theBrand == None) or (len(theBrand) == 0)):
                    responseAll["RetCode"] = "Ret_ERROR_BrandNotFound";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                brandCates = theBrand[0].brandsCates;
                if( len( brandCates )<=0 ):
                    responseAll["RetCode"] = "Ret_ERROR_NoneCategory";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                responseAll["Items"] = aItem 
                responseAll["RetCode"] = "Ret_OK";
            return HttpResponse(json.dumps(responseAll), content_type="application/json")
        elif (typeId == "4"): #品牌主卡(L1Brand) ->子卡(Brand_ClassicSerial)
            brand = request.GET.get("brand","");
            if(brand == ""):
                responseAll["RetCode"] = "Ret_ERROR_Brand";
                return HttpResponse(json.dumps(responseAll), content_type="application/json")
            else:
                brand = brand.encode("utf8")
                brand = urllib.quote(brand)
                aItem = {}
                theBrand = C_Brand.objects.filter(brandName = brand)
                if((theBrand == None) or (len(theBrand) == 0)):
                    responseAll["RetCode"] = "Ret_ERROR_BrandNotFound";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                brandsSerial = theBrand[0].brandsSerial;
                if(len( brandsSerial )<=0 ):
                    responseAll["RetCode"] = "Ret_ERROR_NoneProductItems";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                responseAll["Items"] = aItem 
                responseAll["RetCode"] = "Ret_OK";
            return HttpResponse(json.dumps(responseAll), content_type="application/json")
        elif (typeId == "5"): #品牌主卡(L1Brand) ->子卡(L2Brand_ProductItem) 
            brand = request.GET.get("brand","");
            if(brand == ""):
                responseAll["RetCode"] = "Ret_ERROR_Brand";
                return HttpResponse(json.dumps(responseAll), content_type="application/json")
            else:
                brand = brand.encode("utf8")
                brand = urllib.quote( brand )
                aItem = {}
                theBrand = C_Brand.objects.filter(brandName = brand)
                if((theBrand == None) or (len(theBrand) == 0)):
                    responseAll["RetCode"] = "Ret_ERROR_BrandNotFound";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                ProductItems = theBrand[0].brandsProductItems;
                if(len(ProductItems)<=0 ):
                    responseAll["RetCode"] = "Ret_ERROR_NoneProductItems";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                responseAll["Items"] = aItem 
                responseAll["RetCode"] = "Ret_OK";
            return HttpResponse(json.dumps(responseAll), content_type="application/json")
        else:
            responseAll["RetCode"] = "Ret_ERROR_TypeId_WRONG";
            return HttpResponse(json.dumps(responseAll), content_type="application/json")
