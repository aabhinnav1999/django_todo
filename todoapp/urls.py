from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home-page'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutview,name='logout'),
    path('delete-task/<str:name>/',views.Deletetask,name='delete'),
    path('update/<str:name>/',views.Updatetask,name='update'),
]

