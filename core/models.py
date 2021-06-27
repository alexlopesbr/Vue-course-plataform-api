from django.db import models


class Author(models.Model):
    author = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.author


class Category(models.Model):
    category = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.category


class Course(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    rate = models.FloatField(max_length=255, null=True, blank=True)
    name = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=255, null=False, blank=False)
    price = models.FloatField(max_length=255, null=False, blank=False)
    category = models.ForeignKey(
        Category, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
