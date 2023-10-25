# -*- coding: utf-8 -*-
from django.contrib import admin
from API.models import Insult, InsultReview

all_models = [Insult, InsultReview]
for model in all_models:
    register = admin.site.register(model)
