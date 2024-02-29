from django.shortcuts import render
#from .models import *

from products_app.models import productcls
from .serializers import productSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

#from rest_framework.generics import (
   # ListAPIView,
   # CreateAPIView,
    #RetrieveAPIView,
   # UpdateAPIView, # new
   # DestroyAPIView, # new
#)


# Create your views here.


class productList(APIView):
    authentication_classes=(TokenAuthentication,)
    #list view
    def get(self,request):
        if request.user.is_authenticated:   
            q=productcls.objects.all()
            ser=productSerializer(instance=q,many=True)
            return  Response(ser.data)
        else:
            return  Response({"message":":(توکن برای نمایش وجود ندارد"},status=401)
        
    # Create view     
    def post(self,request):
        if request.user.is_authenticated:
            dser=productSerializer(data=request.data)
            if dser.is_valid():
                dser.save()
                return Response({"status":"success"},status=201)
            return Response(dser.errors)
        else:
            return  Response({"message":":(توکن برای ایجاد کردن وجود ندارد"},status=401)
        
    #update view
    def put(self,request):
        if request.user.is_authenticated:
            i=productcls.objects.get(id=request.data["id"])
            dser=productSerializer(data=request.data,instance=i,partial=True)
            if dser.is_valid():
                dser.save()
                return Response({"status":"success"},status=201)
            return Response(dser.errors)
        else:
            return  Response({"message":":(توکن برای به روز کردن وجود ندارد"},status=401)
        
    #delete view
    def delete(self,request):
        if request.user.is_authenticated:
            i=productcls.objects.get(id=request.data["id"])
            i.delete()
            return Response({"status":"success"},status=201)
        else:
            return  Response({"message":":(توکن برای حذف کردن وجود ندارد"},status=401)
        
# Retrieve view
class productRetrieveView(APIView):
    authentication_classes=(TokenAuthentication,)
    def get(self,request,adad):
        if request.user.is_authenticated:
            q = productcls.objects.get(id=adad)
            ser=productSerializer(instance=q)
            return  Response(ser.data)
        else:
            return  Response({"message":":(توکن برای نمایش وجود ندارد"},status=401)
    




























# Create view
#class productCreateView(CreateAPIView):
    #serializer_class = productSerializer

# List view
#class productListView(ListAPIView):
    #serializer_class = productSerializer
    #queryset = productcls.objects.all() 

# Retrieve view
#class productRetrieveView(RetrieveAPIView):
    #serializer_class = productSerializer
    #queryset = productcls.objects.all() 

# Update view
#class productUpdateView(UpdateAPIView):
    #serializer_class = productSerializer
    #queryset = productcls.objects.all()

# Delete view
#class productDeleteView(DestroyAPIView):
    #serializer_class = productSerializer
    #queryset = productcls.objects.all()          