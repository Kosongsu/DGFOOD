from django.urls import path, include
from .views import index, login_agreed, sign_finish, logout, login, edit_info, menu, menu_add, signup

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('sign_finish/', sign_finish, name="sign_finish"),
    path('edit/', edit_info, name="edit"),
    path('menu/', menu, name="menu"),
    path('menu/add/', menu_add, name="menu_add"),
    path('login/login_agreed/', login_agreed, name="login_agreed"),
    path('login/login_agreed/signup/', signup, name="signup"),




]
