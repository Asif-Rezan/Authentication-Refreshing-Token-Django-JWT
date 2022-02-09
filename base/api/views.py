from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view




@api_view(['GET'])
def getRouts(request):

  routs= [
  '/api/token',
  '/api/token/refresh'
  ]

  return  Response(routs)