from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', 
        views.register, 
        name='register'
        ),
    path('login/', 
        views.loginView, 
        name='login'
        ),
    path(
        'logout/',
        views.logoutView,
        name='logout',
    ),
]