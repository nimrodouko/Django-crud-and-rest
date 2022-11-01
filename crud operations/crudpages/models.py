from django.db import models

class Cases(models.Model):
    Fullname = models.CharField(max_length = 52)
    title = models.CharField(max_length=20)
    
    description =models.TextField()
    images = models.ImageField(upload_to ='images/', null = True, blank =True)
    

    def __str__(self):
        return self.title