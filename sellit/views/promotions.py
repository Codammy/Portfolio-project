from django.http import JsonResponse
from rest_framework.views import status, Response, APIView

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated

from sellit.models.promotions import Promotion
from ..serializers.promotion_serializers import PromotionSerializer

class PromotionView(APIView):

    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )

    """API view"""

    def get(self, request, id=None):
        """get all promotions"""
        if id:
            promotion = Promotion.objects.get_or_404(id=id)
            data = PromotionSerializer(promotion).data
            return JsonResponse(data, status=status.HTTP_200_OK)

        promoter = request.query_params.get("promoter")
        promotions = Promotion.objects.all()

        if promoter:
            promotions = promotions.filter(promoter=promoter)

        data = PromotionSerializer(promotions, many=True).data

        return Response({"data": data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        """create a promotion"""

        # more work to be done on this

        data = dict(request.data)
        data["promoter"] = request.user.id
        promotion = PromotionSerializer(data=data)
        if promotion.is_valid():
            promotion.save()
            return JsonResponse(promotion.data, status=201)
        return JsonResponse(promotion.errors, status=400)

    def delete(self, request, id):
        """deletes a promotion"""

        promotion = Promotion.objects.get_or_404(id)
        if promotion.promoter.id == request.user.id:
            promotion.delete()
            return JsonResponse("promotion successfully deleted", status=200, safe=False)
        return Response(status=400)
