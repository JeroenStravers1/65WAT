from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import RegisteredUser
import datetime

def index(request):
    return render_to_response('logged_in.html')

@csrf_exempt
def login(request):
    context = {}
    return render_to_response('log_in.html', context)

@csrf_exempt
def auth_view(request):
    current_username = request.POST.get('username', '')
    current_password = request.POST.get('password', '')
    # check user exists
    user_exists = get_object_or_404(RegisteredUser, pk=current_username)
    #user_exists = RegisteredUser.objects.get(username=current_username)
    if user_exists is not None:
        #login
        auth.login(request, user_exists)
        return HttpResponseRedirect('/65wat/logged_in/')
    else:
        return HttpResponseRedirect('/65wat/invalid/')

@csrf_exempt
def logout(request):
    return HttpResponse("logout placeholder")

@csrf_exempt
def logged_in(request):
    return HttpResponse("logged_in placeholder")

@csrf_exempt
def invalid(request):
    return HttpResponse("invalid placeholder")

@csrf_exempt
def register(request):
    print('bobobobob')
    return render_to_response('register.html')

@csrf_exempt
def checking(request):
    print('whatevs')
    current_username = request.POST.get('username', '')
    current_password = request.POST.get('password', '')
    # check user exists in db
    try:
        print('user already exists')
        existing_users_with_name = RegisteredUser.objects.get(username=current_username)
        return HttpResponseRedirect('/65wat/invalid/')
    except Exception:
        print('making new user')
        new_user = RegisteredUser(
            username=current_username,
            password=current_password,
            upgrade_lvl=0,
            resource_x=100,
            resource_y=100,
            resource_z=100,
            attack_countdown=datetime.datetime.now(),
            upgrade_countdown=datetime.datetime.now(),
            messages=""
        )
        new_user.save()
        return HttpResponseRedirect('/65wat/login/')
