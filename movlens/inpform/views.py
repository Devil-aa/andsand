from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request,'home.html')

def genres(request):
    return render(request,'test.html')

def keyw(request):
    return render(request,'test.html')

def recomm(request):
    return render(request,'recomm.html')