# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

class ImgInline(admin.TabularInline):
    model=Images


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImgInline,
    ]




myModels=[Person_Register,Category,Chef_Suggest,IsUpdate,Comment2Us,RatingAPi,Images]


admin.site.register(Product,ProductAdmin)

admin.site.register(myModels)

# Register your models here.