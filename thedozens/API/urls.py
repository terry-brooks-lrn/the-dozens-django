# -*- coding: utf-8 -*-
from API import views
from django.urls import path

urlpatterns = [
    path("insults/<str:category>", views.InsultsView.as_view(), name="List_View"),
    path("insult/<int:pk>", views.InsultSingleItem.as_view(), name="Single_View"),
]
