# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from rest_framework.views import exception_handler
from .serializers import *
from .filter import *
import django_filters
from django_filters import rest_framework as filters
from rest_framework.decorators import detail_route
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from django.db.models import Avg
from rest_framework.views import exception_handler
import django_filters.rest_framework
from rest_framework.exceptions import APIException

#########################################################
class UserViewSet(viewsets.ModelViewSet):
    queryset = Person_Register.objects.all()
    serializer_class = PersonSerializer

#########################################################
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
#########################################################
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends=(filters.DjangoFilterBackend,)
    #filter_class = StoreFilter
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

#########################################################
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    filter_backends=(filters.DjangoFilterBackend,)
    filter_class =ImgFilter

#########################################################
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer            
#########################################################
class MainItemViewSet(viewsets.ModelViewSet):
    queryset = MainItem.objects.all()
    serializer_class = MainItemSerializer    
#########################################################
class IsUpdateViewSet(viewsets.ModelViewSet):
    queryset = IsUpdate.objects.all()
    serializer_class = UpdateSerializer
#########################################################
class ProductCommentViewSet(viewsets.ModelViewSet):
    queryset = ProductComment.objects.all()
    serializer_class = ProdctCommentSerializer
    filter_backends=(filters.DjangoFilterBackend,)
    filter_class =CommentFilter
    
#########################################################    
class ReportedCommentViewSet(viewsets.ModelViewSet):
    queryset = ReportedComment.objects.all()
    serializer_class = ReportedCommentSerializer
#########################################################
class Comment2UsViewSet(viewsets.ModelViewSet):
    queryset = Comment2Us.objects.all()
    serializer_class = Comment2UsSerializer
#########################################################
class ChefSuggestViewSet(viewsets.ModelViewSet):
    queryset = Chef_Suggest.objects.all()
    serializer_class = Chef_SuggestSerialize
#########################################################
class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
#########################################################
def custom_exception_handler(exc):

    response = exception_handler(exc)

    if response is not None:
        response.data['status_code'] = response.status_code
    return response

###################################################################
class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'    