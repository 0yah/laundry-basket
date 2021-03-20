from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name="home"),
    path('items',views.ItemListView.as_view(),name="pricelist"),
    path('accounts/register', views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
]