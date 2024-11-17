from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import json

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):
    """
    Manage users via multiple HTTP methods.
    """
    if request.method == 'GET':
        user_nickname = request.GET.get('user')
        if not user_nickname:
            return Response(
                {"error": "User parameter is missing"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            user = User.objects.get(pk=user_nickname)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'POST':
        """
        Create a new user.
        """
        new_user = request.data
        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        """
        Update an existing user by nickname.
        """
        nickname = request.data.get('user_nickname')
        if not nickname:
            return Response(
                {"error": "User nickname is missing"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            updated_user = User.objects.get(pk=nickname)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserSerializer(updated_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_202_ACCEPTED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        """
        Delete a user by nickname.
        """
        try:
            user_to_delete = User.objects.get(pk=request.data['user_nickname'])
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )

    # Handle unsupported methods
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

            
          
        
            
