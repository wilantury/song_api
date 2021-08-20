from django.urls import path
from .views import script_populate

app_name = 'songs'

urlpatterns = [
    path('script_populate', script_populate, name='populate')
]