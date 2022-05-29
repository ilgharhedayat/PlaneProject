from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=125)


class Article(models.Model):
    image = models.ImageField(upload_to='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=1255)
    description = models.TextField()

    def __str__(self):
        return self.title
