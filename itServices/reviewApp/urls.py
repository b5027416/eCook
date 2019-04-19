from django.urls import path
from . import views 

urlpatterns =[

path('', views.home, name='reviewApp-home'),
path('about', views.about, name='reviewApp-about'), 
path('contact',views.contact, name='reviewApp-contact'),
##path('reviews',views.reviews, name='reviewApp-reviews'),
path('report',views.report, name='reviewApp-report'),


]

