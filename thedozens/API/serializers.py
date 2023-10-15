# -*- coding: utf-8 -*-
from rest_framework import serializers
from API.models import Insult


class InsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insult
