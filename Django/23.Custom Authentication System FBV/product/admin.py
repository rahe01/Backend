from django.contrib import admin
from product.models import Product
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):

    model = Product
    list_display = ["id" , "name","price"]
