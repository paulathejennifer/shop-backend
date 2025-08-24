from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogue/', include(router.urls)),
]
