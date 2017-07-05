from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Element(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=False)
    category = models.ManyToManyField(Category, blank=True)
    slide_num = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
