#from django.contrib import admin
from django.contrib.gis import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import CustomUser, Item,Location,Order,OrderDetail,Rider

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('first_name','last_name','email','phone','user_type', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    #Required fields when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class LocationAdmin(admin.OSMGeoAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Item)
admin.site.register(Location,LocationAdmin)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Rider)