from django.urls import path, include
from casa_amparo.new_features.views import MapsTestView

app_name = 'new_features'

urlpatterns = [
    path('maps/', MapsTestView.as_view(), name='maps')
]
