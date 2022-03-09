from django.urls import path
from .views import OrderView, multiple_formsets

urlpatterns = [
    # path('', OrderView.as_view(), name='order'),
    path('', multiple_formsets, name='example_multiple_formsets'),

]
