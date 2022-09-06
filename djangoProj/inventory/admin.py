from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Brand

admin.site.register(Brand)

from .models import Product

admin.site.register(Product)

from .models import Supermarket

admin.site.register(Supermarket)

from .models import Stock

admin.site.register(Stock)