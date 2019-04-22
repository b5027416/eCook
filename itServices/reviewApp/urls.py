from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns =[

path('', views.home, name='reviewApp-home'),
path('about', views.about, name='reviewApp-about'), 
path('register',user_views.register, name='register'),
path('profile', user_views.profile, name='profile'),
path('contact',views.contact, name='reviewApp-contact'),
##path('reviews',views.reviews, name='reviewApp-reviews'),
path('report',views.report, name='reviewApp-report'),

]

