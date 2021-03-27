from django.conf.urls import url
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name="home"),
    path('items',views.ItemListView.as_view(),name="pricelist"),
    path('order',views.order,name="order"),
    path('jsonitems',views.load_items,name="jsonlist"),
    path('jobs',views.jobs,name="jobs"),
    
    path('cart', views.cart,name="cart"),
    url(r'^addcart/(?P<pk>\w{0,50})/$',views.add_cart,name="jsonlist"),
    path('accounts/register', views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
]

r'^addcart/(?P<username>\w{0,50})/$'