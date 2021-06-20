from django.urls import path

from . import views


urlpatterns = [
    path('', views.HouseViewSet.as_view()),
]