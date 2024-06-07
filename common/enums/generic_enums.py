from django.db import models


class Gender(models.TextChoices):
    FEMALE = 'f'
    MALE = 'm'
    OTHER = 'other'




class DocumentType(models.TextChoices):
    ID_PROOF = "Id Proof"
    ADDRESS_PROOF = "Address Proof"
    PROOF_OF_IMCOME = "Proof of Income"
    Age_Proof = "Age Proof"
    Educational_Proof = "Education Proof"

