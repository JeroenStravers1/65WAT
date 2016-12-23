from random import randint

from django.db.backends import sqlite3
from django.shortcuts import render_to_response, _get_queryset
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
    return render_to_response('logged_in.html')
    #return HttpResponse("logged_in placeholder")

@csrf_exempt
def action(request):
    current_attack = request.POST.get('attack', '')
    current_upgrade = request.POST.get('upgrade', '')

    current_user = get_object_or_404(RegisteredUser, pk='arjen')
    current_user_attack_countdown, remainder = divmod(current_user.attack_countdown, 3600)
    current_time, remainder = divmod(datetime.datetime.now(), 3600)
    FMT = '%H:%M:%S'
    test = current_time - current_user_attack_countdown

    time = 2
    if (time > 1):
        if(current_attack == 'attack'):
            all_users = _get_queryset(RegisteredUser)
            selected_number_user = randint(0, len(all_users))
            selected_user = all_users[selected_number_user]
            selected_user_resource_x = selected_user.resource_x
            selected_stolen_resource_x = randint(0, len(selected_user_resource_x))
            remainder_resource_x = selected_user_resource_x - selected_stolen_resource_x
            selected_user.resource_x = remainder_resource_x

            selected_user_resource_y = selected_user.resource_y
            selected_stolen_resource_y = randint(0, len(selected_user_resource_y))
            remainder_resource_y = selected_user_resource_y - selected_stolen_resource_y
            selected_user.resource_y = remainder_resource_y

            selected_user_resource_z = selected_user.resource_z
            selected_stolen_resource_z = randint(0, len(selected_user_resource_z))
            remainder_resource_z = selected_user_resource_z - selected_stolen_resource_z
            selected_user.resource_z = remainder_resource_z

            selected_user.save()

            current_resource_x = current_user.resource_x
            current_user.resource_x = current_resource_x + selected_stolen_resource_x

            current_resource_y = current_user.resource_y
            current_user.resource_y = current_resource_y + selected_stolen_resource_y

            current_resource_z = current_user.resource_z
            current_user.resource_z = current_resource_z + selected_stolen_resource_z

            current_user.save()
            current_action = current_attack
        if(current_upgrade == 'upgrade'):
            current_user_upgrade_lvl = current_user.upgrade_lvl

            current_resource_x = current_user.resource_x
            current_user.resource_x = current_resource_x * current_user_upgrade_lvl + 10

            current_resource_y = current_user.resource_y
            current_user.resource_y = current_resource_y * current_user_upgrade_lvl + 10

            current_resource_z = current_user.resource_z
            current_user.resource_z = current_resource_z * current_user_upgrade_lvl + 10

            current_user.upgrade_lvl = current_user_upgrade_lvl + 1

            current_user.save()


            current_action = current_upgrade

        if(current_attack != 'attack' and current_upgrade !='upgrade'):
            current_action = "No action taken"
            
   # if request.user.is_authenticated():
   #     username = request.user.get_username()
   # else:
   #     username = "test"



    #if(current_user_attack_countdown > current_time):



    password = "test"
    #print (current_action)
    #check global action cooldown timer

    return render_to_response('action.html',{'password':password,'action':current_action,'current_user':test})

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
