from manager.forms import ItemForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.shortcuts import render
from main.models import Order, OrderDetail, Rider, CustomUser, Location, Item, Mpesa
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy



def index(request):
    no_pending_orders = Order.objects.filter(status="IN").count
    no_completed_orders = Order.objects.filter(status="CM").count
    no_orders = Order.objects.all().count
    no_riders = Rider.objects.all().count
    no_items = Item.objects.all().count
    context = {
        "pending_orders": no_pending_orders,
        "completed_orders": no_completed_orders,
        "riders": no_riders,
        "items": no_items,

    }
    return render(request, "manager/index.html", context)

class RiderListView(ListView):
    model = Rider
    template_name = "manager/riders_list.html"

class PendingOrderListView(ListView):
    context_object_name = 'orders'
    model = Order
    queryset = Order.objects.filter(status="IN")
    template_name = "manager/pending/orders_list.html"

class CompleteOrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    queryset = Order.objects.filter(status="CM").all()
    template_name = "manager/complete/orders_list.html"


class OrderDetailView(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = "manager/order_detail.html"


class ItemListView(ListView):
    context_object_name = 'items'
    model = Item
    queryset = Item.objects.all()
    template_name = "manager/item_list.html"

class ItemCreateView(CreateView):
    model = Item
    
    form_class = ItemForm
    
    #fields = ['name','price']
    template_name = "manager/item_form.html"

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    
    #fields = ['name','price']
    success_url = reverse_lazy('items')
    template_name = "manager/item_form.html"



