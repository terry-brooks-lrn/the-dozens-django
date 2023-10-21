# -*- coding: utf-8 -*-
from API.models import Insult
from django_filters import rest_framework as filters


class InsultFilter(filters.FilterSet):
    explicit = filters.BooleanFilter(field_name="explicit")
    category = filters.ChoiceFilter(
        field_name="category", choices=Insult.CATEGORY.choices
    )

    class Meta:
        model = Insult
        fields = {
            "explicit": ["exact"],
            "category": ["exact"],
        }
