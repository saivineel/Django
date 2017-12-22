from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.home, name='home'),
    url(r'^new/$', views.application_new, name='application_new'),
    #url(r'^login/$', views.login, name='login'),
	url(r'^total/$', views.totalregs, name='totalregs'),

	url(r'^regform/$', views.registration, name='registration'),

]