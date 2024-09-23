from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from sellit.views.item import ItemView
from sellit.views.promotions import PromotionView
from sellit.views.store import StoreView
from sellit.views.user import UserView, RegisterView, LoginView, UserProfileView
from sellit.views import commons



urlpatterns = [
    # path("auth"),
    path("feeds", commons.feeds),
    path('token', LoginView.as_view()),
    path('token-refresh', TokenRefreshView.as_view()),
    path('create-account', RegisterView.as_view()),
    path('profile', UserProfileView.as_view()),
    path('profile/<str:id>', UserProfileView.as_view()),

    path("users", UserView.as_view()),
    path("user/<str:id>", UserView.as_view()),

    path("promotions", PromotionView.as_view()),
    path("promotions/<str:id>", PromotionView.as_view()),


    path("store", StoreView.as_view()),
    path("store/<str:id>", StoreView.as_view()),

    path("items", ItemView.as_view()),
    path("items/<str:id>", ItemView.as_view()),
]
