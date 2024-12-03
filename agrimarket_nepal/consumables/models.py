from django.db import models
import os
import time


def image_upload_path(instance, filename):
    ext = filename.split(".")[-1]
    new_filename = f"{instance.name}_{int(time.time())}.{ext}"
    return os.path.join("static/src/storage/images/consumables", new_filename)


class ConsumableType(models.TextChoices):
    Vegetable = "Vegetable"
    Fruit = "Fruit"
    Others = "Others"


# Create your models here.
class Consumable(models.Model):
    class Meta:
        db_table = "consumables"

    name = models.CharField(max_length=200)
    type = models.CharField(choices=ConsumableType)
    calories = models.FloatField()
    seasonal = models.BooleanField()
    image = models.ImageField(null=True, blank=True, upload_to=image_upload_path)
