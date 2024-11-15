"""
URL configuration for FreeWork project.
"""

from django.contrib import admin
from django.urls import path, include
from django.views import generic as django_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        django_views.TemplateView.as_view(template_name="home.html"),
        name="home",
    ),
    path("__debug__/", include("debug_toolbar.urls")),
]
