from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class TestAPI(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Hello, world!"})

    def post(self, request, *args, **kwargs):
        return Response(request.data['name'])
