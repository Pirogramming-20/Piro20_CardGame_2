from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
  path("login/", login_view, name='login'),
  path('logout/', logout_view),
  path('signup/', signup, name='signup'),
]