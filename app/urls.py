
from . import views
from django.conf.urls import url

urlpatterns =[
    url(r'main', views.main),
    url(r'register', views.register),
    url(r'login', views.login),
    url(r'items', views.showItems),
    url(r'about', views.about),
    url(r'contact', views.contact),
    url(r'checkout', views.checkout),
    url(r'single', views.singleItem),
    url(r'exit', views.exit),
    url(r'payment', views.payment),

    url(r'', views.notFount)
]