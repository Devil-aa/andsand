from django.urls import URLPattern, path
from . import views

urlpatterns={
    path('',views.say_hello),
    path('genres',views.genres),
    path('recommend',views.recomm),
    path('keyword',views.keyw)
}