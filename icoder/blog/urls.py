from django.urls import path
from . import views
urlpatterns=[
    path('',views.bloghome, name='bloghome'),
    path('blogpost/',views.blogpost, name='blogpost'),
    path('test/',views.test, name='blogpost'),
    #path ('<str:slug>' , views.blogpost, name='blogpost '),
]