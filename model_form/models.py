from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User_md(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, unique=True)