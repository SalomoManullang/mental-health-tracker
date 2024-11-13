from django.urls import path
from authentication.views import login,register
from authentication.views import logout

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]