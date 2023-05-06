from django.urls import path

from . import views

urlpatterns = [
    path('all_users/', views.GetUser.as_view()),
    path('all_users/<str:pk>', views.UserViewSet.as_view()),
    path('gates/', views.GateAll.as_view()),
    path('gates/<str:pk>', views.GateApi.as_view()),

]