from django.urls import path

from test_gcore.views import get_repo_info

urlpatterns = [
    path('', get_repo_info, name='index'),
]
