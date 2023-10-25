# -*- coding: utf-8 -*-
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
)
from API.filters import InsultFilter
from API.serializers import InsultSerializer, InsultsCategorySerializer
from django_filters import rest_framework as filters
from API.models import Insult
from rest_framework.response import Response
from rest_framework import status
import random
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.permissions import AllowAny

RANDOM_QS = Insult.objects.filter(status="A").values("id", "content").cache(ops=["get"])


@api_view(["GET"])
@permission_classes([AllowAny])
@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def randomUnfilteredInsult(request):
    queryset = list(RANDOM_QS)
    return Response(data=random.choice(seq=queryset), status=status.HTTP_200_OK)


class InsultsView(ListAPIView):
    queryset = Insult.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = InsultFilter
    lookup_field = "category"
    serializer_class = InsultsCategorySerializer


class InsultSingleItem(RetrieveAPIView):
    queryset = Insult.objects.all()
    lookup_field = "id"
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = InsultFilter
    serializer_class = InsultSerializer


class MyInsultsView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        """
        This view returns a list of all insults created by the currently
        authenticated user.

        Returns empty list if user Anonymous
        """
        user = self.request.user

        if not user.is_anonymous:
            return Insult.objects.filter(added_by=user)

        return Insult.objects.none()
