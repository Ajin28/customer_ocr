from django.db import models
from common.models import Country, Customer, DocumentSet
from common.enums.generic_enums import Gender

class CustomerDocument(models.Model):
    document = models.ForeignKey(DocumentSet, on_delete=models.RESTRICT)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    front_image = models.TextField(null=True, blank=True, default=None)
    back_image = models.TextField(null=True, blank=True, default=None)
    extracted_json = models.JSONField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now=True)


