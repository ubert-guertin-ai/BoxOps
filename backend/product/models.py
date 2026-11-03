import uuid
from django.db import models

class Product(models.Model): 
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)

    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2) # 999,999.99
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
