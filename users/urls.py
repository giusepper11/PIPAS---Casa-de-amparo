from django.conf.urls import url
from django.urls import path, include, reverse
from django.utils.functional import lazy

from home.views import SignupProfileView
import allauth.account.views as allauth_account_view

from users.views.pessoa_fisica import pessoa_fisica_signup
from users.views.pessoa_juridica import pessoa_juridica_signup

urlpatterns = [

    url(r"^signuppf/$", pessoa_fisica_signup, name="account_signup_pf"),
    url(r"^signuppj/$", pessoa_juridica_signup, name="account_signup_pj"),

    url(r"^login/$", allauth_account_view.login, name="account_login"),
    url(r"^logout/$", allauth_account_view.logout, name="account_logout"),

    url(r"^password/change/$", allauth_account_view.password_change,
        name="account_change_password"),
    url(r"^password/set/$", allauth_account_view.password_set, name="account_set_password"),

    url(r"^inactive/$", allauth_account_view.account_inactive, name="account_inactive"),

    # E-mail
    url(r"^email/$", allauth_account_view.email, name="account_email"),
    url(r"^confirm-email/$", allauth_account_view.email_verification_sent,
        name="account_email_verification_sent"),
    url(r"^confirm-email/(?P<key>[-:\w]+)/$", allauth_account_view.confirm_email,
        name="account_confirm_email"),

    # password reset
    url(r"^password/reset/$", allauth_account_view.password_reset,
        name="account_reset_password"),
    url(r"^password/reset/done/$", allauth_account_view.password_reset_done,
        name="account_reset_password_done"),
    url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        allauth_account_view.password_reset_from_key,
        name="account_reset_password_from_key"),
    url(r"^password/reset/key/done/$", allauth_account_view.password_reset_from_key_done,
        name="account_reset_password_from_key_done"),

]
