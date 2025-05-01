from django.shortcuts import render, redirect 
from django.http import HttpResponse 
def set_session(request): 
    request.session['username'] = 'john_doe' 
    request.session['favorite_color'] = 'blue' 
    return HttpResponse("Session data set!") 
 
def get_session(request): 
    username = request.session.get('username', 'Guest') # default value if key not found 
    favorite_color = request.session.get('favorite_color', 'unknown') 
    return HttpResponse(f"Username: {username}, Favorite Color: {favorite_color}") 
 
def delete_session(request): 
    try: 
        del request.session['username'] 
        del request.session['favorite_color'] 
    except KeyError: 
        pass # session keys not found, that's ok 
    return HttpResponse("Session data deleted!") 
 
def set_cookie(request): 
    response = HttpResponse("Cookie set!") 
    response.set_cookie('user_id', '12345', max_age=3600) # max_age in seconds 
    return response 
 
def get_cookie(request): 
    user_id = request.COOKIES.get('user_id', 'Cookie not set') 
    return HttpResponse(f"User ID: {user_id}") 
 
def delete_cookie(request): 
    response = HttpResponse("Cookie deleted!") 
    response.delete_cookie('user_id') 
    return response 
 
def session_counter(request): 
    count = request.session.get('count', 0) 
    count += 1 
    request.session['count'] = count 
    return HttpResponse(f"Page visited {count} times (session).") 
 
def cookie_counter(request): 
    count = int(request.COOKIES.get('cookie_count', 0)) 
    count += 1 
    response = HttpResponse(f"Page visited {count} times (cookie).") 
    response.set_cookie('cookie_count', count, max_age=3600) 
    return response 