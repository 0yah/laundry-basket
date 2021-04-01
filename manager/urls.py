from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('orders/pending', views.PendingOrderListView.as_view(), name="orders-pending"),
    path('orders/complete', views.CompleteOrderListView.as_view(), name="orders-complete"),
    path('orders/details/<int:pk>', views.OrderDetailView.as_view(), name="order-details"),
    
    
    path('items', views.ItemListView.as_view(), name="items"),
    path('items/create', views.ItemCreateView.as_view(), name="items-create"),
    path('items/update/<int:pk>', views.ItemUpdateView.as_view(), name="items-update"),
]

r'^addcart/(?P<username>\w{0,50})/$'
