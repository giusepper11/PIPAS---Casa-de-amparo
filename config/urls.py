from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from casa_amparo.home.views import IndexView, SignupProfileView


urlpatterns = [
                  path('', IndexView.as_view(), name='home_page'),
                  path('new_features/', include('casa_amparo.new_features.urls')),
                  path('instituicoes/', include('casa_amparo.instituicoes.urls')),

                  path('users/profsel', SignupProfileView.as_view(), name='account_signup'),
                  path('users/', include('casa_amparo.users.urls')),

                  # path('users/signup/pj', ),
                  # path('users/signup/instituicao', ),

                  path('admin/', admin.site.urls),


] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
