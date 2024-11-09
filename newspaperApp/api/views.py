from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Users,Authors
from .serializer import UsersSerializer,AuthorsSerializer

# Create your views here.
# HTTP REQUEST GET, POST, PUT, DELETE

#APIS To interact with model USERS

@api_view(['GET'])
def users_list(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_user(request):
     serializer = UsersSerializer(data=request.data)
     if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)
     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def users_record(request,pk):
     try:
        user= Users.objects.get(pk=pk)
     except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
     if request.method== 'GET':
         serializer = UsersSerializer(user)
         return Response(serializer.data)
     elif request.method=='PUT':
         serializer = UsersSerializer(user,data = request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
     elif request.method =='DELETE':
         user.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

#APIS To interact with model ATHORS

@api_view(['GET'])
def author_list(request):
    author = Authors.objects.all()
    serializer = AuthorsSerializer(author,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_author(request):
    serializer = AuthorsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def authors_record(request,pk):
     try:
        author= Authors.objects.get(pk=pk)
     except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
     if request.method== 'GET':
         serializer = AuthorsSerializer(author)
         return Response(serializer.data)
     elif request.method=='PUT':
         serializer = AuthorsSerializer(author,data = request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
     elif request.method =='DELETE':
         author.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
         