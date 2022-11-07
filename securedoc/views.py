from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        file = request.FILES['file']
        return HttpResponse(str(file)+"is Uploaded")
    else:
        form = UploadFileForm()

    return render(request,'upload.html',{'form':form})