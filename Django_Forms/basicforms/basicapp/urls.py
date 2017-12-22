from django.conf.urls import url
from . import views

app_name = 'basicapp'

urlpatterns = [

	url(r'^signup/$',views.EmpFormView,name='EmpForm'),
	url(r'^editusers/$',views.EditUsers,name='EditUsers'),
	url(r'^delete/(?P<id>\d+)/$',views.DeleteUser,name='DeleteUser'),

    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
