from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=125)


class Job(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=1255)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Apply(models.Model):
    full_name = models.CharField(max_length=125)
    email = models.EmailField()
    cv = models.FileField(upload_to='')
    phone_number = models.CharField(max_length=11)
    cover_letter = models.CharField(max_length=125)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='apply', null=True, blank=True)

    def __str__(self):
        return self.full_name
