from django.shortcuts import render
from django.http import HttpResponse
# from .forms import InputForm
# Create your views here.
def say_hello(request):
    return render(request,'home.html')

def genres(request):
    # context ={}
    # form= InputForm(request.POST)
    # if form.is_valid():
    
    #     context = {'form': form}
    
    return render(request,'main.html')

def recomm(request):
    print(list(request.POST.items()))
    context={}
    for key,value in request.POST.items():
        context[key]=value

    return render(request,'recomm.html',context)