from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('', views.record_list, name='record_list'), 
    path('create/', views.record_create, name='record_create'), 
    path('update/<int:pk>/', views.record_update, name='record_update'), 
    path('delete/<int:pk>/', views.record_delete, name='record_delete'), 
] 