from product.views import ProductViewSet

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', ProductViewSet, basename="product")

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
