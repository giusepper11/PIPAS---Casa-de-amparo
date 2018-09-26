from django.urls import path, include
from home.views import tempIndex

app_name = 'home'

urlpatterns = [
    path('', tempIndex, name='index')
]
