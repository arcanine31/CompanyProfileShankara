from django.urls import path
from . import views

urlpatterns = [
    path("", views.page, {"page": "home"}, name="home"),
    path("<str:page>/", views.page, name="page"),
]