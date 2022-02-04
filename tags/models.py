from django.db import models
from django.forms import model_to_dict

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add =True)
    update_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.name