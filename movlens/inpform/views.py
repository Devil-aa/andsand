from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import random

# Create your views here.
def say_hello(request):
    return render(request,'home.html')

def genres(request):
    return render(request,'main.html')

def keyw(request):
    return render(request,'test.html')

def recomm(request):
    gen=[i for i in request.POST]
    gen=gen[1:]
    
    df2 = pd.read_csv("C:\\Users\\Agrawal\\Desktop\\movies.csv")

    for i in gen:
        df2=df2.where(df2['genres'].str.contains(i))
        df2=df2.dropna()
    l=list(df2['original_title'])
    random.shuffle(l)
    l=l[:11]

    return render(request,'recomm.html',{'l':l})