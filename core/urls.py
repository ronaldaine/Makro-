from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about/', views.about, name="about"),
]