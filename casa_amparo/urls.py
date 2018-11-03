from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from accounts.views import pessoa_fisica

urlpatterns = [
                  path('', include('home.urls')),
                  path('new_features/', include('new_features.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  # path('accounts/signup/', ),
                  path('accounts/signup/pf', pessoa_fisica.PessoaFisicaSignUpView.as_view(), name='cadastro_pf'),
                  # path('accounts/signup/pj', ),
                  # path('accounts/signup/instituicao', ),
                  path('admin/', admin.site.urls),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
