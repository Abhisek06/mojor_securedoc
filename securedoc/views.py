from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import DocumentForm
from .models import Document
from django.contrib.auth.models import User
import  json
# Create your views here.

def home(request):
    return render(request,'index.html')



def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            some_var = request.POST.getlist('visible')
            curr_title = request.POST.get('title')
            visuser = json.dumps(some_var)
            form.save()
            obj = Document.objects.get(title=curr_title)
            obj.vislist = visuser
            obj.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })