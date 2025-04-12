from django.db import models


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=800)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'about'
