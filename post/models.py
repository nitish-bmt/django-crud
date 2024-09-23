from django.db import models
# from .models import User

# Create your models here.
class Post(models.Model):
    # userId= models.ForeignKey(User, on_delete=models.CASCADE)
    userId = models.CharField(max_length=100)
    title= models.CharField(max_length=100, null=False, blank=False, default='Default Post Title')
    body= models.TextField(null=False, blank=False, default='Lorem')
    likes= models.IntegerField(null=False, blank=False, default=0)
    
    def __str__(self):
        return f'{self.title} by {self.userId} liked by {self.likes}'