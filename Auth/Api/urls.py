from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('' , views.getRoutes),
    path('notes/', views.getNote),
    path('contacts/', views.Contact_list),
    path('contacts/<pk>/', views.contact_detail),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
