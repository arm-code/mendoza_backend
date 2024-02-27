from django.urls import path, include
from rest_framework import routers
from mob_mendoza import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register('forniture', views.MobiliarioView, 'forniture')
router.register('products', views.ProductView, 'products')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title="Mobiliario API"))
]
