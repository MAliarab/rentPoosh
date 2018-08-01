
from . import views
from django.conf.urls import url

urlpatterns =[
    url(r'main', views.main),
    url(r'registration', views.signup),
    url(r'checkform', views.checkForm),
    url(r'loggedin', views.loggedin),
]