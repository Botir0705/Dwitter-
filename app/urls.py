from django.urls import path
from .views import *


urlpatterns = [
    path('dwitter/', index, name='index'),
    path('detail_profile/<int:id>', detail_profile, name='detail_profile'),
    path('all_profiles/', all_profiles, name='all_profiles'),
    path('sign_up/', sign_up, name='sign_up'),
    path('', log_in, name='log_in'),
    path('log_out/', log_out, name='log_out')
]