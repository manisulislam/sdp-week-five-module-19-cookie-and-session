from django.urls import path
from . import views
urlpatterns=[
    path("", views.home, name="home"),
    path("get_cookie/", views.get_cookie, name="get_cookie"),
    path("del_cookie/", views.del_cookie, name="del_cookie"),
    path("index/", views.set_session),
    path("get_session/", views.get_session),
    path("delete_session/", views.delete_session)
]