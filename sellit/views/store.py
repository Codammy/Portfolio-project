from sellit.models import Store
from rest_framework.views import Response, status

from django.http import JsonResponse
from django.core.exceptions import BadRequest
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from ..serializers.store_serializers import StoreSerializer

class StoreView(TokenObtainPairView):
    """Store view"""
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, id=None):
        """returns user store's"""

        if id:
            store = Store.objects.get_or_404(id)
            data = StoreSerializer(store).data
            return JsonResponse(data, status=status.HTTP_200_OK)

        stores = Store.objects.all()

        user_id = request.query_params.get('user')
        if user_id:
            stores = stores.filter(owner=user_id)

        data = StoreSerializer(stores, many=True).data
        return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
    
    def post(self, request):
        """ creates a store for a user"""

        data = dict(request.data)
        data["owner"] = request.user.id
        serializer = StoreSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        """Replace the content of a store to an new one"""


        if not id:
            raise BadRequest("id must be a valid type")
        
        data = dict(request.data)
        data["owner"] = request.user.id
        store = Store.objects.get_or_404(id)
        serializer = StoreSerializer(store, data=data)

        if serializer.is_valid() and request.user.id == store.owner.id:
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
    
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # if not id:
        #     raise HttpResponseBadRequest("id must be a valid type")

    def patch(self, request, id=None):
        """Replace the content of a store to an new one"""


        if not id:
            raise BadRequest('id must be a valid type')
        
        data = dict(request.data)
        data["owner"] = request.user.id

        store = Store.objects.get_or_404(id)

        serializer = StoreSerializer(store, data=data, partial=True)
        if serializer.is_valid() and request.user.id == store.owner.id:
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id):
        """Deletes a store"""

        store = Store.objects.filter(owner=request.user.id, id=id)[0]
        if request.user.id == store.owner.id:
            print(store)
            # Store.objects.delete(store)
        return JsonResponse(status=status.HTTP_200_OK)
