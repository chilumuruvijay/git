from django.urls import path 
from . import views 
urlpatterns = [ 
    path('set_session/', views.set_session, name='set_session'), 
    path('get_session/', views.get_session, name='get_session'), 
    path('delete_session/', views.delete_session, name='delete_session'), 
    path('set_cookie/', views.set_cookie, name='set_cookie'), 
    path('get_cookie/', views.get_cookie, name='get_cookie'), 
    path('delete_cookie/', views.delete_cookie, name='delete_cookie'), 
    path('session_counter/', views.session_counter, name='session_counter'), 
    path('cookie_counter/', views.cookie_counter, name='cookie_counter'), 
] 