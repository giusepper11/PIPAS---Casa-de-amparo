from django.urls import path, include
from home.views import IndexView
from django.views.decorators.cache import never_cache


app_name = 'home'

urlpatterns = [
    path('', never_cache(IndexView.as_view()), name='index'),
]
