from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.shortcuts import render
from main.models import Order, OrderDetail, Rider, CustomUser, Location, Item, Mpesa
from django.views.generic.edit import CreateView,UpdateView,DeleteView,ListView



def index(request):
    no_orders = Order.objects.all().count
    no_riders = Rider.objects.all().count
    no_items = Item.objects.all().count
    context = {
        "orders": no_orders,
        "riders": no_riders,
        "items": no_items,

    }
    render(request, "manager/index.html", context)

class RiderListView(ListView):
    model = Rider
    template_name = "manager/riders_list.html"

class OrderListView(ListView):
    model = Order
    template_name = "orders_list.html"

class ItemCreateView(CreateView):
    model = Item
    template_name = ".html"
