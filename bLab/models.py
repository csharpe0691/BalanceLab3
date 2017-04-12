from django.db import models
from mongoengine import *


# Create your models here.


class Patient(Document):
    header = StringField(required=True)
    version = StringField(max_length=50)
    globals = StringField(max_length=100)
    patient_id = StringField(max_length=15)
    first_name = StringField(max_length=20)
    last_name = StringField(max_length=20)