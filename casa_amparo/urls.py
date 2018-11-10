from django.contrib import admin
from django.urls import path, include, reverse
from django.conf.urls.static import static
from django.conf import settings
from django.utils.functional import lazy
from django.views.decorators.cache import never_cache

from home.views import IndexView, SignupProfileView


urlpatterns = [
                  path('', never_cache(IndexView.as_view()), name='home_page'),
                  path('new_features/', include('new_features.urls')),
                  path('instituicoes/', include('instituicoes.urls')),

                  path('users/profsel', SignupProfileView.as_view(), name='account_signup'),
                  path('users/', include('users.urls')),

                  # path('users/signup/pj', ),
                  # path('users/signup/instituicao', ),

                  path('admin/', admin.site.urls),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
