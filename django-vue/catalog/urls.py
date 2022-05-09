from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path('api/public/', views.public),
    re_path('api/private/', views.private)
]
