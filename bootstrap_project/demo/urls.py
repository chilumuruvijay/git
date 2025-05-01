from django.urls import path
from . import views 
urlpatterns = [ 
    path('', views.sample_page, name='sample_page'), 
] 