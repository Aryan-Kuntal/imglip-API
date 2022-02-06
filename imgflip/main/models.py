from django.db import models

# Create your models here.
class Meme(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    box_count = models.IntegerField()

    def __str__(self):
        return self.name
