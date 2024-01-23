import os
from django.urls import set_urlconf
import pytest
from pytest_django.fixtures import django_db_setup

def pytest_configure():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'Day1Q2.settings'
    set_urlconf('Day1Q2.urls')

pytest_plugins = ["pytest_django"]

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(django_db_setup):
    pass
