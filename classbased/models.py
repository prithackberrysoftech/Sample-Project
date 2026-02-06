from django.db import models

# Create your models here.

class Book(models.Model):
   order = models.IntegerField(default=0)
   title = models.CharField(max_length=50, help_text='Entewr title')
   author = models.CharField(max_length=50, blank=True)
   price = models.DecimalField(max_digits=6, decimal_places=2)
   created_at = models.DateTimeField(auto_now_add=True)
   slug =  models.CharField(max_length=50,blank=True,null=True)

   #Metadata
   class Meta :
       ordering = ['order']


   def __str__(self):
       return self.title
   



from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
