import email
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/',blank=True) 
    
    def __str__(self):
        return self.title
    
class History(models.Model):
    year = models.CharField(max_length=10)
    info = models.CharField(max_length=300)
    
    def __str__(self):
        return self.year
        
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=(
        ('general', 'General'),
        ('event', 'Event'),
        ('health', 'Health'),
        ('tech', 'Technology')
    ),default=None)
    summary = models.CharField(max_length=100, default=None)
    info = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/',blank=True) 
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()
    
    class Meta:
        ordering = ['-id']

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    info = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'), 
        ('female', 'Female')
    ))
    image = models.ImageField(upload_to='images/',blank=True)
    
    def __str__(self):
        return self.name  
    
class Gallery(models.Model):
    info = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=False)
    
    def __str__(self):
        return self.info
    class Meta:
        ordering = ['-id']
    
class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=200, default=None)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['date_added']

    
    def __str__(self):
        return "{} - {}".format(self.post.title, self.name)
    