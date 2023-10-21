# -*- coding: utf-8 -*-
"""
Root URL configuration for thedozens project.
"""
import API.urls
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView
from rest_framework_swagger.views import get_swagger_view
import os
from API.forms import InsultReviewForm

form = InsultReviewForm()
urlpatterns = [
    path(
        "/swagger",
        get_swagger_view(
            title="Your Project",
        ),
        name="swagger",
    ),
    path("/graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/", include(API.urls)),
    re_path(
        r"",
        TemplateView.as_view(
            template_name="index.html",
            extra_context={
                "github_access_token": os.getenv("GITHUB_ACCESS_TOKEN"),
                "ReportForm": form,
            },
        ),
        name="home-page",
    ),
]
