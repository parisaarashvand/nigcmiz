# Create your views here.
from django.shortcuts import render
from . import models

#def miz(request):
#    return render(request, 'nigcMizApp/nigcMizDocs/nigcMiz.html')

def  req_list(request):
    Vreqs = models.MizReqS.objects.all()
    return render(request,'nigcMizApp/nigcMizDocs/esl.html',{'Vreqlist':Vreqs})
