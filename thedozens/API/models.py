# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from loguru import logger
from logtail import LogtailHandler
from django.conf import settings
import os

PRIMARY_LOG_FILE = os.path.join(
    settings.BASE_DIR, "thedozens", "logs", "primary_ops.log"
)
CRITICAL_LOG_FILE = os.path.join(settings.BASE_DIR, "thedozens", "logs", "fatal.log")
DEBUG_LOG_FILE = os.path.join(settings.BASE_DIR, "thedozens", "logs", "utility.log")
LOGTAIL_HANDLER = LogtailHandler(source_token=os.getenv("LOGTAIL_API_KEY"))

logger.add(DEBUG_LOG_FILE, diagnose=True, catch=True, backtrace=True, level="DEBUG")
logger.add(PRIMARY_LOG_FILE, diagnose=False, catch=True, backtrace=False, level="INFO")
logger.add(LOGTAIL_HANDLER, diagnose=False, catch=True, backtrace=False, level="INFO")


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
        LAZY = "L", _("Lazy")
        SHORT = "SRT", _("Short")

    class STATUS(models.TextChoices):
        ACTIVE = "A", _("Active")
        REMOVED = "X", _("Inactive/Removed")
        PENDING = "P", _("Pending")
        REJECTED = "R", _("Rejected")

    content = models.CharField(
        max_length=65535,
        null=False,
        blank=False,
        error_messages="Insults must have content",
    )
    category = models.CharField(
        null=False, blank=False, max_length=5, choices=CATEGORY.choices1
    )
    explicit = models.BooleanField(default=False)
    added_on = models.DateField(null=False, blank=False, auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.PROTECT)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(
        null=False,
        blank=False,
        max_length=2,
        default=STATUS.PENDING,
        choices=STATUS.choices,
    )

    def remove_insult(self):
        """Removes insult visibilitty from the API.

        Logs:
            Success: Logs the PK of the modified Insult Instance
            Exception: If the Insult is unable top be removed.

        Returns:
            None
        """

        try:
            self.status = "X"
            self.last_modified = settings.GLOBAL_NOW
            logger.success(f"Successfully Removed {self.pk}")
        except Exception as e:
            logger.error(f"Unable to Remove Insult ({self.pk}): {e}")

    def approve_insult(self):
        """Adds a Pending insult to the API.

        Updates the Insult.status of the current object to approved, making the current instance discoverable by the API Serializers and Filters.
        Logs:
            Success: Logs the PK of the modified Insult Instance
            Exception: If the Insult is unable top be removed.

        Returns:
            None
        """

        try:
            self.status = "X"
            self.last_modified = settings.GLOBAL_NOW
        except Exception as e:
            logger.error(f"Unable to Remove Insult: {e}")

    def mark_insult_for_review(self):
        """Removes insult visibilitty from from the API.

        Logs:
            Exception: If the Insult is unable top be removed.

        Returns:
            None
        """

        try:
            self.status = "X"
        except Exception as e:
            logger.error(f"Unable to Remove Insult: {e}")

    def remove_insult(self):
        """Removes insult visibilitty from from the API.

        Logs:
            Exception: If the Insult is unable top be removed.

        Returns:
            None
        """

        try:
            self.status = "X"
        except Exception as e:
            logger.error(f"Unable to Remove Insult: {e}")
