from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import random
import imdb
ia = imdb.IMDb()

# Create your views here.
def say_hello(request):
    return render(request,'home.html')

def genres(request):
    return render(request,'checkbox.html')

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

    df2=df2.sample(frac = 1)
    df3=df2.head(10)
    poster=[]

    for i in list(df3['title']):

        try:
            series = ia.search_movie(i)
            for i in range(len(series)):
                id = series[i].movieID
            series = ia.get_movie(id)
            cover = series.data['cover url']
            poster.append(cover)
        except:
            poster.append("../static/images/632144.png")


    l=[]
    for i in range(len(list(df3['title']))):
        t=[]
        try:
            search_results = ia.search_movie(list(df3['title'])[i])
            if search_results:
                movieID = search_results[0].movieID
                movie = ia.get_movie(movieID)
                
                if movie:
                    cast = movie.get('cast')
                    topActors = 5
                    for actor in cast[:topActors]:
                        t.append("'{0} as {1}' ".format(actor['name'], actor.currentRole))
        except:
            pass


        l.append({'poster':poster[i],
                'title':list(df3['title'])[i],
                'rating':str(list(df3['vote_average'])[i]),
                'director':list(df3['director'])[i],
                'runtime':str(list(df3['runtime'])[i]),
                'date':list(df3['release_date'])[i],
                'description':list(df3['overview'])[i]
                ,'cast':t})
                
        #l.append([list(df3['title'])[i],list(df3['vote_average'])[i],list(df3['director'])[i],list(df3['runtime'])[i],list(df3['release_date'])[i],list(df3['overview'])[i],list(df3['cast'])[i]])
    return render(request,'recomm.html',{'l':l})