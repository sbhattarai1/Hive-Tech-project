from django.contrib import admin

# Register your models here.
@admin.register(cart)
class CartModel(admin.ModelAdmin):
    fields = ['user','product','quantity']
    list_filter = []
    list_display = fields
    search_fields=['user','producr']