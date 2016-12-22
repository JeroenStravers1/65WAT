from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt




from django.http import HttpResponse

@csrf_protect
def index(request):
    return render_to_response('logged_in.html')


@csrf_exempt
def login(request):
    context = {}
    return render_to_response('log_in.html', context)

    #c = {}
    #c.update(request)
    #return render_to_response('log_in.html', RequestContext(request, {}))

@csrf_exempt
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    # check user exists
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        #login
        auth.login(request, user)
        return HttpResponseRedirect('/65wat/logged_in/')
    else:
        return HttpResponseRedirect('/65wat/invalid/')

def logout(request):
    return HttpResponse("logout placeholder")

def logged_in(request):
    return HttpResponse("logged_in placeholder")

def invalid(request):
    return HttpResponse("invalid placeholder")

def register(request):
    return render_to_response('register.html')

def registering(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    # check user exists in db
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        # login
        auth.login(request, user)
        return HttpResponseRedirect('/65wat/logged_in/')
    else:

        #TODO user creation here
        return HttpResponseRedirect('/65wat/invalid/')
