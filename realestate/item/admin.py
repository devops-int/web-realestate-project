from django.contrib import admin

from .models import Catergory, Item, Currency
# Register your models here.

admin.site.register(Catergory)
admin.site.register(Item)
admin.site.register(Currency)