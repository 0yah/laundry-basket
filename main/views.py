from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views import generic
from .models import Item
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required,permission_required
from .forms import CustomUserCreationForm

# Create your views here.
def index(request):
    return render(request,'main/index.html')


def register(request):

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        #If the form is valid save the user and redirect them
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(reverse('home'))


    context = {
        'form':form,
    }
    return render(request,'registration/register.html',context)

class ItemListView(generic.ListView):
    model = Item
    template_name = 'main/item_list.html'

