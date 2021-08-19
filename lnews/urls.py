from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as rest_views
from rest_framework.routers import DefaultRouter

from lnews import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()

router.register('news', viewset=views.NewsViewSet)
router.register('categories', viewset=views.NewsCategoryViewSet)
urlpatterns = []

urlpatterns += [
    path('api/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
