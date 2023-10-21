# -*- coding: utf-8 -*-
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
)
from API.filters import InsultFilter
from API.serializers import InsultSerializer, InsultsCategorySerializer
from django_filters import rest_framework as filters
from rest_framework.exceptions import NotFound
from rest_framework import status
from API.models import Insult
from rest_framework.response import Response
import random

# Create your views here.


class InsultsView(
    ListCreateAPIView,
):
    queryset = Insult.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = InsultFilter
    serializer_class = InsultsCategorySerializer

    def get_queryset(self, category="fat"):
        insults = Insult.objects.filter(status="A").filter(category=category)
        return insults


class InsultSingleItem(RetrieveUpdateDestroyAPIView):
    queryset = Insult.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = InsultFilter
    serializer_class = InsultSerializer

    def get_object(self, pk):
        try:
            Response(data=Insult.objects.get(id=pk), status=status.HTTP_200_OK)
        except NotFound:
            Response(
                data={"error": "No Item with that ID exisits in the API"},
                status=status.HTTP_404_NOT_FOUND,
            )
