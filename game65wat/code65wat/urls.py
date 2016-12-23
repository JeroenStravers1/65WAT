from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),

    # user auth urls
    url(r'^login', views.login, name='login'),
    url(r'^auth', views.auth_view, name='auth'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^logged_in', views.logged_in, name='logged_in'),
    url(r'^action', views.action, name='action'),
    url(r'^invalid', views.invalid, name='invalid'),
    url(r'^register', views.register, name='register'),
    url(r'^checking', views.checking, name='checking'),
]