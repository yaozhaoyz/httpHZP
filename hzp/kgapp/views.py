## coding=utf8
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from hzp.settings import URL_PREFIX 
from models import *
import urllib2
import datetime
import os
import json
import re
import heapq
import random

class MyHeap(object):
    def __init__(self, initial=None, key=lambda x:x):
        self.k = 10 
        self.key = key
        self._data = []
    def push(self, item):
        if len(self._data) < self.k:
            heapq.heappush(self._data, (self.key(item), item))
        else:
            topk_small = list(self._data[0])
            if item.a > topk_small[1].a:
                heapq.heapreplace(self._data, (self.key(item), item))
    def pop(self):
        if(len(self._data)>=1):
            return heapq.heappop(self._data)[1]
        else:
            return None

class Element():
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

def importData2Product(request):
    responseAll = {};
    StarPHeap = {} # 明星产品
    cate = {} # 类目
    product = {}
    serial = {}
    FuncTag ={}
    p_b={}
    p_guige = {}
    p_gongxiao = {}
    p_serial={}
    p_jieshao = {}
    p_jiage = {}
    p_score = {}
    p_skin = {}
    p_age ={}
    p_age_1 ={}
    count_age_1={}
    p_age_2 ={}
    count_age_2={}
    p_age_3 ={}
    count_age_3={}
    p_age_4 ={}
    count_age_4={}
    p_age_5 ={}
    count_age_5={}
    p_pl = {}
    p_pl = {}
    p_link={}
    responseAll["Product"] = "";
    for line in open("/disk1/hzpDjango/data/product.txt"): 
        line = line.replace("&quot","").replace("&nbsp","")
        line = line.replace("<","").replace(">","");
        line = line.replace("&","")
        line = line.split("\t");
        p = line[0]
        b = line[1].lower().strip()
        name = b;
        c = line[2];
        found = C_Brand.objects.filter(brandName = b)
        if(found == None or len(found)==0):
            aBrand = C_Brand(brandName = name)
            aBrand.brandsProductItems= []
            aBrand.brandsProductItems.append(p)
            aBrand.brandsCates= []
            aBrand.brandsCates.append(c)
            aBrand.save();
        else:
            aBrand = C_Brand.objects.get( brandName = name )
            aBrand.brandsProductItems.append(p)
            aBrand.brandsCates.append(c)
            aBrand.save();
        if b not in p_b:
            p_b[b] = 1;
        else:
            p_b[b] += 1;
        p_guige[p] = line[3] 
        p_gongxiao[p] =  line[5]
        p_serial[p]=line[4]
        p_jieshao[p] = line[6] 
        p_jiage[p]= line[7]
        p_score[p]= line[8]
        p_skin[p]= line[9]
        p_age[p]= line[10]
        p_pl[p]= line[13]
        p_link[p]= line[16]
        # new a product. 
        aPid = Pid(pid=0)
        aPid.save();
        productId = len(Pid.objects)
        aProduct = C_Product(ProductId = productId)
        aProduct.ProductName= p;
        aProduct.ProductImgURL = line[18].strip();
        aProduct.ProductDaPei = line[19].strip();
        aProduct.ProductCategory= c;
        aProduct.ProductBrand = b;
        aProduct.ProductAge= {};
        aProduct.ProductGongxiao = [];
        aProduct.ProducePrice = p_jiage[p];
        aProduct.ProduceScore = p_score[p];
        for i in p_gongxiao[p].split(" "):
            if(i != ""):
                aProduct.ProductGongxiao.append(i);
        try:
            aProduct.ProductPLScore = float(p_pl[p]);
        except:
            aProduct.ProductPLScore = 0.0
        aProduct.ProductJieshao = p_jieshao[p];
        aProduct.ProductUsage = line[12].strip();
        aProduct.ProductLinkURL = p_link[p] 
        age_str = line[10].replace("20以下","20below")
        age_str = age_str.replace("20-25岁","25below")
        age_str = age_str.replace("26-30岁","30below")
        age_str = age_str.replace("31-40岁","40below")
        age_str = age_str.replace("40以上","45below")
        if( age_str != ""):
            r = re.compile('20below (.*?)%')
            if(b not in p_age_1):
                p_age_1[b] = float(r.findall(age_str)[0])
                count_age_1[b] = 1 
            else:
                p_age_1[b] += float(r.findall(age_str)[0]) 
                count_age_1[b] += 1 
            aProduct.ProductAge["20below"] = p_age_1[b];
            r = re.compile('25below (.*?)%')
            if(b not in p_age_2):
                p_age_2[b] = float(r.findall(age_str)[0])
                count_age_2[b] = 1 
            else:
                p_age_2[b] += float(r.findall(age_str)[0]) 
                count_age_2[b] += 1 
            aProduct.ProductAge["25below"] = p_age_2[b];
            r = re.compile('30below (.*?)%')
            if(b not in p_age_3):
                p_age_3[b] = float(r.findall(age_str)[0])
                count_age_3[b] = 1 
            else:
                p_age_3[b] += float(r.findall(age_str)[0]) 
                count_age_3[b] += 1 
            aProduct.ProductAge["30below"] = p_age_3[b];
            r = re.compile('40below (.*?)%')
            if(b not in p_age_4):
                p_age_4[b] = float(r.findall(age_str)[0])
                count_age_4[b] = 1 
            else:
                p_age_4[b] += float(r.findall(age_str)[0]) 
                count_age_4[b] += 1 
            aProduct.ProductAge["40below"] = p_age_4[b];
            r = re.compile('45below (.*?)%')
            if(b not in p_age_5):
                p_age_5[b] = float(r.findall(age_str)[0])
                count_age_5[b] = 1 
            else:
                p_age_5[b] += float(r.findall(age_str)[0]) 
                count_age_5[b] += 1 
            aProduct.ProductAge["45below"] = p_age_5[b];
        aProduct.save();
        #responseAll["Product"] += aProduct.ProductName+";"
    responseAll["Brand"] = []
    for line in open("/disk1/hzpDjango/data/brand.dat"):
        line = line.strip().split("");
        name = line[0].lower().strip()
        jieshao = line[1]
        img = line[2]
        place = line[3]
        year = line[4]
        website = line[5]
        found = C_Brand.objects.filter( brandName = name)
        if(found == None or len(found)==0):
            aBrand = C_Brand(brandName = name)
            responseAll["Brand"].append(name);
            aBrand.brandPlace = place;
            aBrand.brandBirthday = year;
            aBrand.brandGuanwang = website;
            aBrand.brandImg = img
            aBrand.brandJieshao = jieshao
            aBrand.save();
        else:
            aBrand = found[0]
            aBrand.brandPlace = place;
            aBrand.brandBirthday = year;
            aBrand.brandGuanwang = website;
            aBrand.brandImg = img
            aBrand.brandJieshao = jieshao
            aBrand.save();
    responseAll["RetCode"]="Ret_OK";
    responseAll["ProductNum"]=len(C_Product.objects)
    return HttpResponse(json.dumps(responseAll), content_type="application/json") 

def brandSearch(request):
    if(request.method == 'GET'):
        return render_to_response('brandMain.html',{}, context_instance=RequestContext(request))

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
                brand_raw = urllib2.unquote(brand).encode("utf8") # now,it is utf8
                brand = urllib2.quote(brand_raw)
                aItem = {}
                aItem["BrandName"] = brand_raw;
                aItem["StarProduct"] = str(URL_PREFIX)+"/hzp/main/?fromcard=L1Brand&tocard=L2Brand_StarProduct&typeId=2&brand="+brand;
                aItem["CategoryList"]= str(URL_PREFIX)+"/hzp/main/?fromcard=L1Brand&tocard=L2Brand_Category&typeId=3&brand="+brand;
                aItem["ClassicSerial"]= str(URL_PREFIX)+"/hzp/main/?fromcard=L1Brand&tocard=L2Brand_ClassicSerial&typeId=4&brand="+brand;
                aItem["brandsProductItems"]= str(URL_PREFIX)+ "/hzp/main/?fromcard=L1Brand&tocard=L2Brand_brandsProductItems&typeId=5&brand="+brand;
                responseAll["Items"] = aItem 
                responseAll["RetCode"] = "Ret_OK";
                theBrand = C_Brand.objects.filter(brandName = brand_raw)
                if((theBrand == None) or (len(theBrand) == 0)):
                    responseAll["RetCode"] = "Ret_ERROR_BrandNotFound";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                aBrand =  theBrand[0]
                pre= "<html><head><title>品牌主卡L1Brand</title>"
                suf= "</head></html>"
                out = pre;
                out += "<li><img src=\""+aBrand.brandImg.encode("utf8")+"\"></img></li>"
                out += "<li><a>品牌名："+aItem["BrandName"]+"</a></li>"
                out += "<li><a>发源地："+aBrand.brandPlace.encode("utf8")+"</a></li>"
                out += "<li><a>起源于："+aBrand.brandBirthday.encode("utf8")+"</a></li>"
                out += "<li><a>官网："+aBrand.brandGuanwang.encode("utf8")+"</a></li>"
                out += "<li><a>品牌介绍："+aBrand.brandJieshao.encode("utf8")+"</a></li>"
                out += "<li><a href=\""+aItem["StarProduct"]+"\">明星产品</a></li>"
                out += "<li><a href=\""+aItem["CategoryList"]+"\">产品类目</a></li>"
                out += "<li><a href=\""+aItem["ClassicSerial"]+"\">经典系列</a></li>"
                out += "<li><a href=\""+aItem["brandsProductItems"]+"\">产品大全</a></li>"
                out += suf;
                return HttpResponse(out)
#return HttpResponse(json.dumps(responseAll), content_type="application/json")
        elif (typeId == "2"): #品牌主卡(L1Brand) ->子卡(L2Brand_StarProduct) 
            brand = request.GET.get("brand","");
            if(brand == ""):
                responseAll["RetCode"] = "Ret_ERROR_Brand";
                return HttpResponse(json.dumps(responseAll), content_type="application/json")
            else:
                brand = brand.encode("utf8")
                brand = urllib2.quote( brand )
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
                brand = urllib2.unquote(brand).encode("utf8")
                theBrand = C_Brand.objects.filter(brandName = brand)
                if((theBrand == None) or (len(theBrand) == 0)):
                    responseAll["RetCode"] = "Ret_ERROR_BrandNotFound";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                brandCates = theBrand[0].brandsCates;
                if( len( brandCates )<=0 ):
                    responseAll["RetCode"] = "Ret_ERROR_NoneCategory";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                responseAll["Items"] = brandCates  
                pre= "<html><head><title>品牌类目L1BrandCate</title>"
                suf= "</head></html>"
                out = pre;
                out += "<br>品牌类目L1Brand_Category_Product</br>"
                for i in brandCates:
                    out += "<li><a href=\""+"http://115.28.9.133:8088/hzp/main/?fromcard=L2Brand_Category&tocard=L1Brand_Category_Product&typeId=9&cate="+i.encode("utf8")+"&brand="+brand+"\">"+i.encode("utf8")+"</a></li>"
                out += suf
                return HttpResponse(out)
                responseAll["RetCode"] = "Ret_OK";
            return HttpResponse(json.dumps(responseAll), content_type="application/json")
        elif (typeId == "4"): #品牌主卡(L1Brand) ->子卡(Brand_ClassicSerial)
            brand = request.GET.get("brand","");
            if(brand == ""):
                responseAll["RetCode"] = "Ret_ERROR_Brand";
                return HttpResponse(json.dumps(responseAll), content_type="application/json")
            else:
                brand = brand.encode("utf8")
                brand = urllib2.quote(brand)
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
        elif (typeId == "5"):#romcard=L1Brand&tocard=L2Brand_ProductItem&brand=兰蔻&typeId=5  
            brand = request.GET.get("brand","");
            if(brand == ""):
                responseAll["RetCode"] = "Ret_ERROR_productId";
                return HttpResponse(json.dumps(responseAll), content_type="application/json")
            else:
                brand = brand.encode("utf8")
                theProduct = C_Product.objects.filter(ProductBrand = brand)
                if((theProduct == None) or (len(theProduct) == 0)):
                    responseAll["RetCode"] = "Ret_ERROR_ProductNotFound";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                pre= "<html><head><title>产品详情</title>"
                suf= "</head></html>"
                out = pre;
                out += "<br>产品详情</br>"
                out += "<br></br>"
                for i in theProduct:
                    out += "<li><img src=\""+str(i.ProductImgURL.strip())+"\"></img></li>"
                    out += "<li><a>Name: "+str(i.ProductName.encode("utf8"))+"</a></li>"
                    out += "<li><a>漂亮指数: "+str(i.ProductPLScore)+"<a></li>"
                    out += "<li><a>链接地址: "+str(i.ProductLinkURL)+"</a></li>"
                    out += "<li><a>产品介绍: "+str(i.ProductJieshao.encode("utf8"))+"</a></li>"
                    out += "<li><a>适合肤质: "
                    for j in i.ProductSkin:
                        out += str(j)+" "
                    out += "</a></li>"
                    if(i.ProductPrice != None):
                        out += "<li><a>价格: "+str(i.ProductPrice.encode("utf8"))+"</a></li>"
                    if(i.ProductScore!= None):
                        out += "<li><a>综合评价: "+str(i.ProductScore.encode("utf8"))+"</a></li>"
                    #out += "<li><a>适合年龄: "+str(i.ProductAge)+"</a></li>"
                    if(i.ProductUsage!= None):
                        out += "<li><a>使用方法: "+str(i.ProductUsage.encode("utf8"))+"</a></li>"
                    if(i.ProductDaPei!= None):
                        out += "<li><a>最佳搭配: "+str(i.ProductDaPei.encode("utf8"))+"</a></li>"
                out += suf
                return HttpResponse(out)
                responseAll["RetCode"] = "Ret_OK";
        elif (typeId == "9"):#romcard=L1Brand&tocard=L2Brand_ProductItem&brand=兰蔻&typeId=5  
            brand = request.GET.get("brand","");
            cate = request.GET.get("cate","");
            if((brand == "")or(cate =="")):
                responseAll["RetCode"] = "Ret_ERROR_productId";
                return HttpResponse(json.dumps(responseAll), content_type="application/json")
            else:
                brand = brand.encode("utf8")
                cate = cate.encode("utf8")
                theProduct = C_Product.objects.filter(ProductBrand=brand,ProductCategory=cate)
                if((theProduct == None) or (len(theProduct) == 0)):
                    responseAll["RetCode"] = "Ret_ERROR_ProductNotFound";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                pre= "<html><head><title>产品列表</title>"
                suf= "</head></html>"
                out = pre;
                out += "<br>产品详情</br>"
                out += "<br></br>"
                for i in theProduct:
                    out += "<li><img src=\""+str(i.ProductImgURL.strip())+"\"></img></li>"
                    out += "<li><a>Name: "+str(i.ProductName.encode("utf8"))+"</a></li>"
                    out += "<li><a>漂亮指数: "+str(i.ProductPLScore)+"<a></li>"
                    out += "<li><a>链接地址: "+str(i.ProductLinkURL)+"</a></li>"
                    out += "<li><a>产品介绍: "+str(i.ProductJieshao.encode("utf8"))+"</a></li>"
                    out += "<li><a>适合肤质: "
                    for j in i.ProductSkin:
                        out += str(j)+" "
                    out += "</a></li>"
                    if(i.ProductPrice != None):
                        out += "<li><a>价格: "+str(i.ProductPrice.encode("utf8"))+"</a></li>"
                    if(i.ProductScore!= None):
                        out += "<li><a>综合评价: "+str(i.ProductScore.encode("utf8"))+"</a></li>"
                    #out += "<li><a>适合年龄: "+str(i.ProductAge)+"</a></li>"
                    if(i.ProductUsage!= None):
                        out += "<li><a>使用方法: "+str(i.ProductUsage.encode("utf8"))+"</a></li>"
                    if(i.ProductDaPei!= None):
                        out += "<li><a>最佳搭配: "+str(i.ProductDaPei.encode("utf8"))+"</a></li>"
                out += suf
                return HttpResponse(out)
                responseAll["RetCode"] = "Ret_OK";
        
        elif (typeId == "10"):#romcard=L1Brand&tocard=L2Brand_ProductItem&brand=兰蔻&typeId=5  
            productId = request.GET.get("productId","");
            if(productId == ""):
                responseAll["RetCode"] = "Ret_ERROR_productId";
                return HttpResponse(json.dumps(responseAll), content_type="application/json")
            else:
                theProduct = C_Product.objects.filter(ProductId = productId)
                if((theProduct == None) or (len(theProduct) == 0)):
                    responseAll["RetCode"] = "Ret_ERROR_ProductNotFound";
                    return HttpResponse(json.dumps(responseAll), content_type="application/json")
                pre= "<html><head><title>产品详情</title>"
                suf= "</head></html>"
                out = pre;
                out += "<br>产品详情</br>"
                out += "<br></br>"
                for i in theProduct:
                    out += "<li><img src=\""+str(i.ProductImgURL.strip())+"\"></img></li>"
                    out += "<li><a>Name: "+str(i.ProductName.encode("utf8"))+"</a></li>"
                    out += "<li><a>漂亮指数: "+str(i.ProductPLScore)+"<a></li>"
                    out += "<li><a>链接地址: "+str(i.ProductLinkURL)+"</a></li>"
                    out += "<li><a>产品介绍: "+str(i.ProductJieshao.encode("utf8"))+"</a></li>"
                    out += "<li><a>适合肤质: "
                    for j in i.ProductSkin:
                        out += str(j)+" "
                    out += "</a></li>"
                    if(i.ProductPrice != None):
                        out += "<li><a>价格: "+str(i.ProductPrice.encode("utf8"))+"</a></li>"
                    if(i.ProductScore!= None):
                        out += "<li><a>综合评价: "+str(i.ProductScore.encode("utf8"))+"</a></li>"
                    #out += "<li><a>适合年龄: "+str(i.ProductAge)+"</a></li>"
                    if(i.ProductUsage!= None):
                        out += "<li><a>使用方法: "+str(i.ProductUsage.encode("utf8"))+"</a></li>"
                    if(i.ProductDaPei!= None):
                        out += "<li><a>最佳搭配: "+str(i.ProductDaPei.encode("utf8"))+"</a></li>"
                out += suf
                return HttpResponse(out)
                responseAll["RetCode"] = "Ret_OK";
        else:
            responseAll["RetCode"] = "Ret_ERROR_TypeId_WRONG";
            return HttpResponse(json.dumps(responseAll), content_type="application/json")
