# coding=gbk
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, render
from django_ajax.decorators import ajax
from models import *
import heapq
import datetime
import os
import json

# Create your views here.
def test(request):
    responseAll = {}
    responseAll["test"]="hello world";
    return HttpResponse(json.dumps(responseAll), content_type="application/json")
