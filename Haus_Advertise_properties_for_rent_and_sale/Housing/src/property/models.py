from django.db import models

# Create your models here.
property_type = {
    ('sale','sale'),
    ('rent','rent')
}

class Property(models.Model):
    owner_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    description = models.TextField()
    location = models.CharField(max_length=70)
    type_of_property = models.CharField(max_length=5,choices=property_type)
    price = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    category = models.ForeignKey('Category',null=True,on_delete=models.SET_NULL)
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/',null = True)
    approved = models.BooleanField(default=False)
    

    def __str__(self):
        return self.owner_name
    
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Reserve(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    notes  = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
    
    


    

