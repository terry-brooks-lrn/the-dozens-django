# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Insult(models.Model):
    class CATEGORY(models.TextChoices):
        POOR = "P", _("Poor")
        FAT = "F", _("Fat")
        UGLY = "U", _("Ugly")
        STUPID = "S", _("Stupid/Dumb")
        SNOWFLAKE = "SNWF", _("Snowflake")
        OLD = "O", _("Old")
        DADDY_OLD = "DO", _("Old/Daddy")
        DADDY_STUPID = "DS", _("Stupid/Daddy")
        NASTY = "N", _("Nasty")
        TALL = "T", _("Stupid/Dumb")
        TESt_CATAGORY = "TEST", _("Testing")
        SKINNY = "SKN", _("Skinny")
        BALD = "B", _("Bald")
        HAIRY = "H", _("Hairy")

    class STATUS(models.TextChoices):
        ACTIVE = "A", _("Active")
        REMOVED = "X", _("Inactive/Removed")
        PENDING = "P", _("Pending")
        REJECTED = "R", _("Rejected")

    content = models.CharField(
        max_length=65535,
        null=False,
        required=True,
        error_messages="Insults must have content",
    )
    category = models.CharField(
        required=True, max_length=5, choices=CATEGORY.choices, null=False, blank=False
    )
    explicit = models.BooleanField(default=False)
    added_on = models.DateField(required=True, auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.PROTECT)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(
        required=True,
        max_length=2,
        default=STATUS.PENDING,
        choices=STATUS.choices,
        null=False,
        blank=False,
    )
