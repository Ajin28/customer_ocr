from django.db import models
from common.models import Country

# created by admin
class DocumentSet(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    country = models.ManyToManyField(Country)
    has_backside = models.BooleanField(default=False)
    ocr_labels = models.JSONField(null=True, default=None, blank=True) # This Json is a key value pair of potentially available data from this document.