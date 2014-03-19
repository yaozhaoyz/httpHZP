#coding=utf8
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
for line in open("result"): #sys.argv[1]
    line = line.replace("&quot","").replace("&nbsp","")
    line = line.replace("<","").replace(">","");
    line = line.replace("&","")
    line = line.split("\t");
    p = line[0]
    b = line[1];
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
        r = re.compile('25below (.*?)%')
        if(b not in p_age_2):
            p_age_2[b] = float(r.findall(age_str)[0])
            count_age_2[b] = 1 
        else:
            p_age_2[b] += float(r.findall(age_str)[0]) 
            count_age_2[b] += 1 
        r = re.compile('30below (.*?)%')
        if(b not in p_age_3):
            p_age_3[b] = float(r.findall(age_str)[0])
            count_age_3[b] = 1 
        else:
            p_age_3[b] += float(r.findall(age_str)[0]) 
            count_age_3[b] += 1 
        r = re.compile('40below (.*?)%')
        if(b not in p_age_4):
            p_age_4[b] = float(r.findall(age_str)[0])
            count_age_4[b] = 1 
        else:
            p_age_4[b] += float(r.findall(age_str)[0]) 
            count_age_4[b] += 1 
        r = re.compile('45below (.*?)%')
        if(b not in p_age_5):
            p_age_5[b] = float(r.findall(age_str)[0])
            count_age_5[b] = 1 
        else:
            p_age_5[b] += float(r.findall(age_str)[0]) 
            count_age_5[b] += 1 
    p_pl[p]= line[13]
    p_link[p]= line[16]
    if(b not in cate):
        cate[b] = {}
    if(line[2] not in cate[b]):
        cate[b][line[2]]=[]
    cate[b][line[2]].append(line[0]);
    if(b not in serial):
        serial[b] = {}
    if(line[4] not in serial[b]):
        serial[b][line[4]]=[]
    serial[b][line[4]].append(line[0]);
    if(p_pl[p]==""):
        pl = 0.0;
    else:
        pl = float(p_pl[p]);
    if(b not in StarPHeap):
        StarPHeap[b] = MyHeap(key=lambda item:item.a) # 明星产品
    StarPHeap[b].push(Element(pl,p,b)); #top 20 plScore StarProduct.
#    if(b not in cate):
#        cate[b] = {}
#    if(line[2] not in cate[b]):
#        cate[b][line[2]]=[]
#    cate[b][line[2]].append(line[0]);
#for aTag in re.split(r" |/", line[6]): 
#       if(b in FuncTag):
#           FuncTag[b].append(aTag);
#       else:
#           FuncTag[b] = []

fout = open("fout.txt","w");
print "<hzp>"
print "<brands>"
for b in cate:
    print "<brand>"
    print b
    fout.write(b+"\t"+str(p_b[b])+"\n");
    print "<cates>"
    for i in cate[b]:
        print "<cate>"
        print i
        for j in cate[b][i]:
            print "<product>"
            print j
            print "<guige>"+p_guige[j]+"</guige>"
            print "<gongxiao>"+p_gongxiao[j]+"</gongxiao>"
            print "<jieshao>"+p_jieshao[j]+"</jieshao>"
            print "<jiage>"+p_jiage[j]+"</jiage>"
            print "<score>"+p_score[j]+"</score>"
            print "<skin>"+p_skin[j]+"</skin>"
            print "<age>"+p_age[j]+"</age>"
            print "<pl>"+p_pl[j]+"</pl>"
            print "<link>"+p_link[j]+"</link>"
            print "</product>"
        print "</cate>"
    print "</cates>"
    print "<serials>"
    for i in serial[b]:
        print "<serial>"
        print i
        for j in serial[b][i]:
            print "<product>"
            print j
            print "<guige>"+p_guige[j]+"</guige>"
            print "<gongxiao>"+p_gongxiao[j]+"</gongxiao>"
            print "<jieshao>"+p_jieshao[j]+"</jieshao>"
            print "<jiage>"+p_jiage[j]+"</jiage>"
            print "<score>"+p_score[j]+"</score>"
            print "<skin>"+p_skin[j]+"</skin>"
            print "<age>"+p_age[j]+"</age>"
            print "<pl>"+p_pl[j]+"</pl>"
            print "<link>"+p_link[j]+"</link>"
            print "</product>"
        print "</serial>"
    print "</serials>"
    print "<StarProducts>"
    StarP = [] 
    for i in range(10):
        k = StarPHeap[b].pop()
        if(k!=None):
            StarP.insert(0,k.b)
    for m in StarP:
        j = m  #  product name;
        print "<StarProduct>"
        print j
        print "<guige>"+p_guige[j]+"</guige>"
        print "<gongxiao>"+p_gongxiao[j]+"</gongxiao>"
        print "<jieshao>"+p_jieshao[j]+"</jieshao>"
        print "<jiage>"+p_jiage[j]+"</jiage>"
        print "<score>"+p_score[j]+"</score>"
        print "<skin>"+p_skin[j]+"</skin>"
        print "<age>"+p_age[j]+"</age>"
        print "<pl>"+p_pl[j]+"</pl>"
        print "<link>"+p_link[j]+"</link>"
        print "</StarProduct>"
    print "</StarProducts>"
    print "<avg_age>"
    if b in count_age_1:
        print "<age_1>"+str(p_age_1[b]/count_age_1[b])+"</age_1>"
        print "<age_2>"+str(p_age_2[b]/count_age_2[b])+"</age_2>"
        print "<age_3>"+str(p_age_3[b]/count_age_3[b])+"</age_3>"
        print "<age_4>"+str(p_age_4[b]/count_age_4[b])+"</age_4>"
        print "<age_5>"+str(p_age_5[b]/count_age_5[b])+"</age_5>"
    print "</avg_age>"
    print "</brand>"
print "</brands>"

print "</hzp>"
