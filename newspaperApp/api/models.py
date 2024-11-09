from django.db import models

# Create your models here.

class Users (models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    def __str__(self):
        return self.name
    
class Authors(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    newpaper_name= models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name

class Articles(models.Model):
    author = models.ForeignKey(Authors,related_name='articles',on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=255,null=True)
    content = models.TextField(null=True)
    published_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.title
class Comments(models.Model):
    article=models.ForeignKey(Articles,related_name='comments',on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(Users,related_name='comments',on_delete=models.CASCADE,null=True)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.content