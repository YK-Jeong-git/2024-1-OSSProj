from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.



# DRF 방식
@api_view()
def sign_up(request):
    return Response({'message':'Hello_world'})

