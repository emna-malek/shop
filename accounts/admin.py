from django.contrib import admin
from .models import Customer
from .models import userProfile

# Register your models here.

admin.site.register(Customer)


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['name', ]


admin.site.register(userProfile)
