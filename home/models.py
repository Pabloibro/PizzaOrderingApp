from django.db import models
from django.contrib.models import User
import uuid



# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class PizzaCategory(BaseModel):
    category_name = models.CharField(max_length = 100)

class Pizza(BaseModel):
    c
