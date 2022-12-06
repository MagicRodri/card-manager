import uuid

from django.db import models

# Create your models here.



class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, auto_created=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']