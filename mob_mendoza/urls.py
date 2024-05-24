from django.urls import path, include
from rest_framework import routers
from mob_mendoza import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register('forniture', views.MobiliarioView, 'forniture')
router.register('customers', views.CustomerView, 'customers')
router.register('products', views.ProductView, 'products')
router.register('cart', views.CartView, 'cart')
router.register('address', views.AddressView, 'address')
router.register('order', views.OrderView, 'order')
router.register('order-detailed', views.OrderDetailedView, 'order-datailed')
router.register('order-check', views.OrderListView, 'order-check')
router.register('packs', views.ComponentView, 'packs')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title="Mobiliario API"))
]
