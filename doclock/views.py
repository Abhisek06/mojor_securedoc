from django.shortcuts import render,redirect
from django.http import HttpResponse
from securedoc.forms import DocumentForm
from securedoc.models import Document
import json

# Create your views here.

def home(request):
    context = {}
    doc_all = Document.objects.all()
    context['document'] = doc_all
    jsonDec = json.decoder.JSONDecoder()
    for obj in doc_all:
        perlist = jsonDec.decode(obj.vislist)
        obj.vislist = perlist
        count = 0
        for i in obj.vislist:
            obj.vislist[count] = int(obj.vislist[count])
            count=count+1

    return render(request,'index.html',context)