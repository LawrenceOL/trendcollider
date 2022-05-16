from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    path("stock_list/", views.stock_list, name="stock_list"),
    path("api/public", views.public, name="public"),
    path("api/private", views.private, name="private"),
    path("weigh_ins", views.weigh_ins, name="weigh_ins"),
    path("weigh_in_detail/<id>", views.weigh_in_detail, name="weigh_in_detail"),
    path("add_weigh_in/", views.add_weigh_in, name="add_weigh_in"),
    #  views.add_weigh_in, name = "add_weigh_in"),
]
