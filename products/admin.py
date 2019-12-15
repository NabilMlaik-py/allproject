from django.contrib import admin
from .models import Product, Promo


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class PromoAdmin(admin.ModelAdmin):
    list_display = ('Code', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Promo, PromoAdmin)

