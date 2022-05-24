from django.urls import URLPattern, path
from . import views

urlpatterns={
    path('',views.say_hello),
    path('recommend',views.recomm)
}