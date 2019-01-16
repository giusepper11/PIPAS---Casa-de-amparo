import pytest
from django.conf import settings
from django.test import RequestFactory

pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    def test_get_success_url(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        pass

    def test_get_object(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        pass

class TestUserRedirectView:

    def test_get_redirect_url(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        pass
