from django.urls import path, include
from rest_framework import routers
from mob_mendoza import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register('forniture', views.MobiliarioView, 'forniture')
router.register('products', views.ProductView, 'products')
router.register('clients', views.ClientView, 'clients')
router.register('address', views.AddressView, 'addresss')
router.register('cart', views.ShoppingCartView, 'cart-create')
router.register('cart-items', views.CartItemView, 'cartitems-create')
router.register('purchase-order', views.PurchaseOrderView, 'purchase-order')
router.register('detailed-order', views.DetailedOrderView, 'detailed-order')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title="Mobiliario API"))
]
