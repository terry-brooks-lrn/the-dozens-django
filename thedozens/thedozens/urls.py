# -*- coding: utf-8 -*-
"""
Root URL configuration for thedozens project.
"""
from API.forms import InsultReviewForm
from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path, re_path
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.views.generic import TemplateView
from ghapi.all import GhApi
from logtail import LogtailHandler
from loguru import logger
from rest_framework import status
from rest_framework.response import Response
from rest_framework_swagger.views import get_swagger_view
import API.urls
import graphQL.urls
import os

PRIMARY_LOG_FILE = os.path.join(settings.BASE_DIR, "standup", "logs", "primary_ops.log")
CRITICAL_LOG_FILE = os.path.join(settings.BASE_DIR, "standup", "logs", "fatal.log")
DEBUG_LOG_FILE = os.path.join(settings.BASE_DIR, "standup", "logs", "utility.log")
LOGTAIL_HANDLER = LogtailHandler(source_token=os.getenv("LOGTAIL_API_KEY"))

logger.add(DEBUG_LOG_FILE, diagnose=True, catch=True, backtrace=True, level="DEBUG")
logger.add(PRIMARY_LOG_FILE, diagnose=False, catch=True, backtrace=False, level="INFO")
logger.add(LOGTAIL_HANDLER, diagnose=False, catch=True, backtrace=False, level="INFO")


# @cache_page(timeout=43200, key_prefix="index")
def home(request):
    context = dict()
    form = InsultReviewForm()
    context["ReportForm"] = form
    return render(request, "index.html", context)


def create_github_issue(request):
    if request.method == "POST":
        form = InsultReviewForm(request.POST)
        if form.is_valid():
            try:
                issue_body = form.cleaned_data["rationale_for_review"]
                issue_title = f"New Joke Review (Joke Id: {form.cleaned_data['insult_id']}) - {form.cleaned_data['review_type']}"
                GITHUB_API = GhApi(
                    owner="terry-brooks-lrn",
                    repo="the-dozens-django",
                    token=os.getenv("GITHUB_ACCESS_TOKEN"),
                )
                GITHUB_API.issue.create(title=issue_title, body=issue_body)
                logger.success(
                    f"successfully submitted Joke: {form.cleaned_data['insult_id']} for review"
                )
                return Response(data={"status": "OK"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                logger.error(
                    f"Unable to Submit {form.cleaned_data['insult_id']} For Review: {str(e)}"
                )
                return Response(
                    data={"status": "FAILED"}, status=status.HTTP_417_EXPECTATION_FAILED
                )
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


urlpatterns = [
    path(
        "swagger",
        get_swagger_view(
            title="Your Project",
        ),
        name="swagger",
    ),
    path("graphql", include("graphQL.urls"), name="GraphQL"),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/", include(API.urls)),
    path("home", home, name="home-page"),
    path("report-joke", create_github_issue, name="Report-Joke"),
]
