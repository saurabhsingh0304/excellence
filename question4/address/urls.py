from django.urls import path
from . import views as v

urlpatterns = [
    path('register/', v.register_page, name='register'),
    path('login/', v.loginpage, name='login'),
    path('', v.home, name='home'),
    path('logout/', v.logoutuser, name='logout')
]