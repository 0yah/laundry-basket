import json
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .models import Item, Location, Order, OrderDetail
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CartForm, CustomUserCreationForm, LoginForm
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


def signin(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            print(user)
            login(request, user)
            return redirect(reverse('home'))

    form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/login.html', context)


class ItemListView(generic.ListView):
    model = Item
    context_object_name = "items"
    template_name = 'main/item_list.html'


def order(request):
    return render(request, 'main/order.html')


def load_items(request):
    """

    del request.session['pks']
    del request.session['items']
    del request.session['total']

    """

    pks = request.session.get("pks", [])

    items = serializers.serialize("json", Item.objects.exclude(pk__in=pks))
    data = json.loads(items)

    return JsonResponse(data, safe=False)


def isAdded(list, item):
    try:
        t = list.index(item)
        return t
    except ValueError:
        return False


def add_cart(request, pk):

    # Get saved Items IDs
    pks = request.session.get("pks", [])
    # Store saved Items IDs
    request.session['pks'] = pks

    inCart = isAdded(pks, pk)

    # If the item is already in the cart return the correct items
    if inCart:
        items = serializers.serialize("json", Item.objects.exclude(pk__in=pks))
        data = json.loads(items)
        print(len(data))
        return JsonResponse(data, safe=False)

    pks.append(pk)
    items = Item.objects.exclude(pk__in=pks).values_list('pk', flat=True)

    # Find the item
    add_item = Item.objects.get(pk=pk)
    print(add_item)
    # Get cart items from session
    cart_items = request.session.get("items", [])
    # Add item to session
    cart_items.append({'pk': add_item.pk, 'name': add_item.name,
                       'price': add_item.price, 'quantity': 1})
    # Save the session
    request.session['items'] = cart_items

    print(cart_items)

    # Get the total
    total = request.session.get("total", 0)
    # Add the total
    request.session['total'] = add_item.price + total

    items = serializers.serialize("json", Item.objects.exclude(pk__in=pks))
    data = json.loads(items)
    return JsonResponse(data, safe=False)


def cart(request):
    cart_items = request.session.get("items")
    pks = request.session.get("pks")
    items = Item.objects.filter(id__in=pks)
    [print(item.pk) for item in items]

    [print(cart_items[index]["quantity"], cart_item)
     for index, cart_item in enumerate(items)]

    form = CartForm()

    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            cart_items = request.session.get("items")
            total_price = request.session.get("total")
            pks = request.session.get("pks")

            pin = form.cleaned_data['pin']
            street = form.cleaned_data['street']
            floor = form.cleaned_data['floor']
            apt = form.cleaned_data['apt']

            orderLocation = Location(
                pin=pin, street=street, apt=apt, floor=floor)
            orderLocation.save()
            order = Order(location=orderLocation,
                          customer=request.user, price=total_price)
            order.save()
            print(orderLocation)

            items = Item.objects.filter(id__in=pks)
            orderDetails = [OrderDetail(item=cart_item, order=order, quantity=cart_items[index]
                                        ["quantity"]) for index, cart_item in enumerate(items)]

            OrderDetail.objects.bulk_create(orderDetails)

    context = {
        'form': form
    }

    return render(request, 'main/cart.html', context)


def jobs(request):
    context = {
        'title': 'Careers'
    }
    return render(request, 'main/jobs.html', context)
