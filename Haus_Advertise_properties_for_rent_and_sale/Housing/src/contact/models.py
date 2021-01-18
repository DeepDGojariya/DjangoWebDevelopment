from django.db import models

# Create your models here.
class ContactDetails(models.Model):
    #location = 
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Contact Details'
        verbose_name_plural = 'Contact Details'
