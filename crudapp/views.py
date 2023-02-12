from django.shortcuts import render
from crudapp.models import College 
from crudapp.serializers import CollegeSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status 

@api_view(['POST'])
def create(request):
    
    serilaizer = CollegeSerializer(data=request.data)
    if serilaizer.is_valid(raise_exception=True):
        serilaizer.save()
        return Response(serilaizer.data) 
    
@api_view(['GET'])
def list(request):
    clg = College.objects.all()
    serializer = CollegeSerializer(clg,many=True)
    return Response(serializer.data)
    
    
@api_view(['PUT'])
def update(request , id):
    clg = College.objects.get(pk = id)
    seriaiizer = CollegeSerializer(clg,data=request.data)
    if seriaiizer.is_valid(raise_exception=True):
        seriaiizer.save()
        return Response(seriaiizer.data) 
    
    
@api_view(['PATCH'])
def updates(request , id):
    clg = College.objects.get(pk = id)
    seriaiizer = CollegeSerializer(clg,data=request.data)
    if seriaiizer.is_valid(raise_exception=True):
        seriaiizer.save()
        return Response(seriaiizer.data) 
    
@api_view(['DELETE'])
def delete(request, id):
    clg = College.objects.get(pk=id)
    clg.delete()
    return Response({'delete':'data has been deleted'}) 