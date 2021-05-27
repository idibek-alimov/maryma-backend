from django.db import models
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=30,
                            db_index=True)
    slug = models.SlugField(max_length=30,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.slug)
        super().save(*args,**kwargs)    



class SubCategory (models.Model):
    category = models.ForeignKey(Category,
                                 related_name='category',
                                 on_delete=models.CASCADE)  
    name = models.CharField(max_length=30,
                            db_index=True)
    slug = models.SlugField(max_length=30,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.slug)
        super().save(*args,**kwargs)

SIZES = (
        ('XS', 'ExtraSmall'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'ExtraLarge'),
        ('XXL', '2ExtraLarge'),
    )
class Product (models.Model):
    author = models.ForeignKey(get_user_model(),
                               #settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,
                                 related_name='subcategory',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    description = models.TextField()
  
    size = ArrayField(models.CharField(max_length=10,blank=True,null=True)) 
    #MultiSelectField(choices=SIZES,
    #                        null=True, blank=True)
    #colors = ArrayField(models.CharField(choices=SIZES,max_length=10,blank=True,null=True))
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    image = models.ImageField(upload_to='img',null=True,blank=True)


    available = models.BooleanField(default=True)

    created = models.DateField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Like (models.Model):
    #user_id = models.IntegerField()
    user = models.ForeignKey(get_user_model(),
                                on_delete=models.CASCADE)
    product_id = models.IntegerField()
    
    def __str__(self):
        return str(self.user)