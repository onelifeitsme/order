from django.urls import path
from .views import OrderView, LoadProducts

urlpatterns = [
    path('', OrderView.as_view(), name='order_page'),
    path('ajax/load-products/', LoadProducts.as_view(), name='ajax_load_products'),
]
