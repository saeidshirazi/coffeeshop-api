from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from model_utils import Choices
import computed_property
from django_jalali.db import models as jmodels

# Create your models here.

class Person_Register(models.Model):
     created=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now_add=True)
     name = models.CharField(max_length=100, default='')
     phone_number = PhoneNumberField(default='')
     def __str__(self):
         return self.name


class Category(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='media', null=True)
    cat_name = models.CharField(max_length=100, default='')
    def __str__(self):
         return self.cat_name

class Product(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    product_name= models.CharField(max_length=100, default='')
    catid =  models.ForeignKey(Category, on_delete=models.CASCADE,default='coffeeshop',related_name='catid')
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True, default='')
    mainpic=models.ImageField(upload_to='media', null=True)
    
class Chef_Suggest(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    p_suggest=models.ForeignKey(Product, on_delete=models.CASCADE,default='1',related_name='p_suggest')
    def __str__(self):
        return str(self.p_suggest)


class Images(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    product_image=models.ForeignKey(Product, on_delete=models.CASCADE,default='1',related_name='pro_image')
    image = models.ImageField(upload_to='media', null=True)
    def __str__(self):
        return str(self.product_image)    

class IsUpdate(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    version = models.CharField(max_length=100, default='')
    isupdate= models.BooleanField(default=True)
    url =  models.URLField(default="https://telegram.me/CyberSTM", max_length=200)
    def __str__(self):
        return self.version
class ProductComment(models.Model):
    created=jmodels.jDateField(auto_now_add=True,blank=True)
    updated_at=jmodels.jDateField(auto_now_add=True,blank=True)
    usercm_id=models.ForeignKey(Person_Register, on_delete=models.CASCADE,default='1',related_name='usercm_id')
    productcm_id=models.ForeignKey(Product, on_delete=models.CASCADE,default='1',related_name='productcm_id')
    username= models.CharField(max_length=100, default='',null=True)
    cm =models.TextField(blank=True, null=True, default='')
    def __str__(self):
        return str(self.usercm_id)
class Comment2Us(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    comment =models.TextField(blank=True, null=True, default='')
    p_id=models.ForeignKey(Person_Register, on_delete=models.CASCADE,default='1',related_name='p_id')
    def __str__(self):
        return str(self.p_id)

class RatingAPi(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    product_qm=models.ForeignKey(Product, on_delete=models.CASCADE,default='1',related_name='product_qm')
    user_qm=models.ForeignKey(Person_Register, on_delete=models.CASCADE,default='1',related_name='user_qm')
    price_choice=Choices(
    (5,'excellent'),
    (4,'very good'),
    (3,'average'),
    (2,'bad'),
    (1,'awful'),
    )
    price_rate=models.IntegerField(choices=price_choice,default=5)

    quality_choice=Choices(
    (5,'excellent'),
    (4,'very good'),
    (3,'average'),
    (2,'bad'),
    (1,'awful'),
    )

    quality_rate=models.IntegerField(choices=quality_choice,default=5)
    def total_rate(self):
        sum=self.price_rate+self.quality_rate
        return sum / 2.0
    total=computed_property.ComputedFloatField(compute_from='total_rate',default=-1)

    class Meta:
       unique_together = (('product_qm', 'user_qm'),)
       ordering= ("-total",)

    def __str__(self):
        return str(self.user_qm)   
