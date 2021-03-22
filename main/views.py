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

    items = serializers.serialize("json", Item.objects.all())
    data = json.loads(items)
    return JsonResponse(data, safe=False)


def add_cart(request, pk):
    add_item = Item.objects.get(pk=pk)
    #request.session['total'] = add_item.price

    test_cart = [
        {'name': 'Ian', 'price': 9},
        {'name': 'Jan', 'price': 19},
        {'name': 'sdkjnkj', 'price': 9}
    ]

    test_new_data = {
                {'name': 'Ian', 'price': 9}
    }

    print(test_new_data in test_cart)
    #request.session['items'] = add_item.price

    #print()

    items = serializers.serialize("json", Item.objects.all())
    data = json.loads(items)
    return JsonResponse(data, safe=False)
