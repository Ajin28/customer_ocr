from django.db import models
from common.models import Country, CustomUser
from common.enums.generic_enums import Gender
# from django.contrib.auth.hashers import make_password, check_password


class Customer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.OTHER.value)
    age = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now=True)
    
    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)
    
    # def check_password(self, raw_password):
    #     return check_password(raw_password, self.password)

