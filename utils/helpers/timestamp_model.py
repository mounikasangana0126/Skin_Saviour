"""Timestamp Model."""

# pylint: disable=E0401,R0903


from django.db import models

class TimeStampedModel(models.Model):
    """A TimeStampedModel."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(blank=False, null=False, default=True)

    class Meta:
        """Meta data for the table."""

        abstract = True
