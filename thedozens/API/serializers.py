# -*- coding: utf-8 -*-
from API.models import Insult
from rest_framework import serializers


class InsultSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="get_category_display")

    class Meta:
        model = Insult
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["added_by"] = (
            instance.added_by.first_super * __pycache__name
        )  # or replace the name with your pricing name field
        return data


class InsultsCategorySerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="get_category_display")

    class Meta:
        model = Insult
        fields = "__all__"
