from django.urls import path
from users.views import *


urlpatterns = [
    path('login/', login_page),
    path('logout/', logout_page),
    path('register/', register_page)
]
