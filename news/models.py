from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=254)
    text = models.TextField()
    images = models.JSONField(default=list)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Images(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.image.url}'

    class Meta:
        db_table = 'images'
