from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status  # To edit the message after POST method.

from .models import SysAdmin
from REST_API.serializers import PostSerializer


# This function will be rendered in HTML
def home(request):
    list = SysAdmin.objects.all()
    context = {
        'admins': list
    }
    return render(request, 'home.html', context)


# >>>>>>>>>> API View <<<<<<<<<<<<<<<
# We need to call the api_view function for API view
# We don't need to create any html.
# We imported PostSerializer class from the serializer.py


# Functions for API: sys_admin, sys_admin_details

# This API endpoint is for Create and List.
@api_view(['GET', 'POST'])  # This decorator will render the API View
def sys_admin(request):
    # List
    if request.method == "GET":  # Using the GET method.
        list = SysAdmin.objects.all()  # We are calling all the data in models.py
        serializer = PostSerializer(list, many=True)  # We now serialize the list.

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # status cannot be any custom string.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This API endpoint is for RUD: Retrieve, Update, Delete.
@api_view(['GET', 'PUT', 'DELETE'])  # This decorator will render the API View
def sys_admin_details(request, pk):
    # try and except are for handling error. Like when an item does not exist.
    try:
        list = SysAdmin.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Retrieve
    if request.method == 'GET':
        serializer = PostSerializer(list)  # we area serializing the list
        return Response(serializer.data)

    # Update
    elif request.method == 'PUT':
        serializer = PostSerializer(list, data=request.data)  # Update the list with request.data
        if serializer.is_valid():
            serializer.save()
            # status cannot be any custom string.
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete
    elif request.method == 'DELETE':
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
