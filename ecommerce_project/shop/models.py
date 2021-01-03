from django.db import models
from django.db.models.fields import related

# Create your models here.
class Category(models.Model):
    '''
        Represents a Category (of :class:`shop.models.Product` )
        
        :param name: self-explanatory
        :type name: string
        :param slug: easy name for pretty URL
        :type slug: string
    '''
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    '''
        Represents a Product to be sold. It is related with one :class:`shop.models.Category`
        
        :param category: OneToMany field relation with :class:`shop.models.Category`
        :type category: :class:`shop.models.Category`
        :param name: self-explanatory
        :type name: string
        :param slug: easy name for pretty URL
        :type name: string
        :param image: an image of the product
        :type image: image file
        :param description: a description of the product
        :type description: string, optional
        :param price: self-explanatory
        :type price: decimal (float) with maximum 10 digits
        :param available: a boolean field indicating if the product is available
        :type available: boolean, default True
        :param created: The date and time when the product was first added to the system
        :type created: DateTime
        :param updated: The last date and time when the product was modified
        :type updated: DateTime
    '''
    category=models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)# Automatically set the field to now when the object is first created. 
    updated=models.DateTimeField(auto_now=True) # Automatically set the field to now every time the object is saved.

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

