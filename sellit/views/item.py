from django.http import JsonResponse
from rest_framework.views import APIView, Response, status

from sellit.models.item import Item
from sellit.models.store import Store
from sellit.serializers.item_serializers import ItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class ItemView(APIView):
    """product view"""

    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )

    def get(self, request, id=None):
        """get all products"""
    
        serializer = {}

        
        if id:
            item = Item.objects.get_or_404(id=id)
            serializer = ItemSerializer(item)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)

        items = Item.objects.all()
        store = request.query_params.get("store")

        if store:
            items = items.filter(store=store)
            
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    
    def post(self, request):
        """add an item to a store"""

        serializer = ItemSerializer(data=request.data)

        store = request.data.get("store")
        store = Store.objects.get(id=store)

        if serializer.is_valid() and (store.owner.id == request.user.id):
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
         """replace existing values with a new one"""

         item = Item.objects.get_or_404(id)
         serializer = ItemSerializer(item, data=request.data)

         store = Store.objects.get_or_404(item.store)
         if serializer.is_valid() and (store.owner.id == request.user.id):
              serializer.save()
              return JsonResponse(serializer.data, status=status.HTTP_200_OK)
         return JsonResponse(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        """replace existing values with a new one"""

        item = Item.get_or_404(id)

        store = Store.objects.get_or_404(item.store)
        serializer = ItemSerializer(item, data=request.data, partial=True)

        if serializer.is_valid() and (store.owner.id == request.user.id):
             serializer.save()
             return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        """Deletes an item from a store"""

        item = item.objects.get_or_404(id)
        if item.store.owner == request.user.id:
            item.delete()
            return JsonResponse(status=status.HTTP_200_OK)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, safe=False)
    