from django.db import models
from django.contrib.auth.models import User



class Articles(models.Model):
    name_author = models.CharField(max_length=255, default='')
    title = models.CharField('Title', max_length=50)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date of publication')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/user/news'
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    born_date = models.DateField(null=True, blank=True)
    born_location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return '/user/authors'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return '/user/quotes'
    
