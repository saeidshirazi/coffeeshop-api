from .models import *
from rest_framework import serializers
import datetime
from django_jalali.db import models as jmodels


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person_Register
        fields = ('id','name','phone_number')
###################################################################
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = ('id','product_name','description','catid','quantity','price','mainpic')
###################################################################
class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Images
        fields = ('id','product_image','image')

###################################################################
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','cat_name','photo')
###################################################################
class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=IsUpdate
        fields=('id','version','isupdate','url')                
###################################################################
class ProdctCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductComment
        fields=('id','created','updated_at','usercm_id','productcm_id','username','cm')
###################################################################
class Comment2UsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Comment2Us
        fields =('id','created','updated_at','comment','p_id') 

class Chef_SuggestSerialize(serializers.ModelSerializer):
    class Meta:
        model = Chef_Suggest
        fields =('id','created','updated_at','p_suggest') 
                  