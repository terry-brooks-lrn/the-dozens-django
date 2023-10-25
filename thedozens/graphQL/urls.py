# -*- coding: utf-8 -*-
from graphene_django.views import GraphQLView
from django.urls import path
from graphQL.schema import schema

urlpatterns = [
    path("", GraphQLView.as_view(graphiql=True, schema=schema)),
]
