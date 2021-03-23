import json
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .models import Item
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.core import serializers

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def register(request):

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        # If the form is valid save the user and redirect them
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))

    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context)


class ItemListView(generic.ListView):
    model = Item
    context_object_name = "items"
    template_name = 'main/item_list.html'


def order(request):
    return render(request, 'main/order.html')


def load_items(request):

    testMe =Item.objects.all().values_list('pk', flat=True)

    teste =Item.objects.exclude(pk__in=[2,3]).values_list('pk', flat=True)
    #print(teste)
    
    #print(testMe)

    items = serializers.serialize("json", Item.objects.all())
    data = json.loads(items)
    return JsonResponse(data, safe=False)


def add_cart(request, pk):
    teste =Item.objects.exclude(pk__in=[2,3]).values_list('pk', flat=True)
    #print(teste)

    #Find the item
    add_item = Item.objects.get(pk=pk)
    
    print(add_item)
    #Get cart items from session
    cart_items = request.session.get("items", [])
    #Add item to session
    cart_items.append({'pk':add_item.pk,'name': add_item.name, 'price': add_item.price})
    #Save the session
    request.session['items'] = cart_items

    print(cart_items)

    #Get the total
    total = request.session.get("total", 0)
    #Add the total
    request.session['total'] = add_item.price + total


    #Store saved Items IDs
    pks = request.session.get("pks", [])
    pks.append(pk)
    request.session['pks'] = pks


    items = serializers.serialize("json", Item.objects.all())
    data = json.loads(items)
    return JsonResponse(data, safe=False)
