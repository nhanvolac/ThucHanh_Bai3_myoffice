from django.contrib import admin
from django.urls import path
from officemaster import views
#import django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('blog.html', views.blog, name="blog"),
    path('contact.html', views.contact, name="contact"),
    path('team.html', views.team, name="team"),
]