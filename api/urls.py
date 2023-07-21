from django.urls import path

from . import views

urlpatterns = [
    path('my/pulses', views.pulses, name="pulses"),
    path('users/<str:name>', views.users, name="users"),
]
