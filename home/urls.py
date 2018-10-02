from django.urls import path, include
from home.views import IndexView

app_name = 'home'

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
