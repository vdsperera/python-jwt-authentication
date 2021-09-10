from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from .services import UsersService;

# Create your views here.
# class UsersView(APIView):
#   def get(self, request):
#       return Response(request.get_full_path());


class UsersView(viewsets.ModelViewSet):

    def register(self, request):
        data = request.data;
        # print(data)
        user_service = UsersService()
        response = user_service.register(data)
        return Response(response);

    def login(self, request):
        data = request.data
        user_service = UsersService()
        token = user_service.login(data);

        response_data = {
            "message": "success",
            "token": token,
            }

        response = Response()
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = response_data
        return response;

    def get_user(self, request):
        user_service = UsersService()
        response = user_service.get_user(request)
        return Response(response)

    def logout(self, request):
        user_service = UsersService()

        response = Response()
        response.delete_cookie('jwt')

        response_data = {
          "message": "Successfully Logout"
        }
        response.data = response_data
        return response;