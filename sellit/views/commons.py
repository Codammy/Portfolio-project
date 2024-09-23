from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.views import status

@api_view(['GET'])
def feeds(request):
    return JsonResponse([], status=status.HTTP_200_OK)