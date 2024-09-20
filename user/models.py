from django.db import models

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=50, blank=False, null=False)
  last_name = models.CharField(max_length=50)
  username = models.CharField(max_length=100, unique=True, blank=False, null=False)
  email = models.EmailField(unique=True, blank=False, null=False)
  password = models.CharField(max_length=20, blank=False, null=False)

  def __str__(self):
    return f'{self.username}: {self.first_name} {self.last_name}'
  # def __str__(self) -> str:
  #   return super().__str__()
