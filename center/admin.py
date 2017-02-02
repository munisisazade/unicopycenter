from django.contrib import admin
from center.models import Orders
# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'number', 'email','date')
    list_filter = ('date',)
    search_fields = ('full_name',)

admin.site.register(Orders,OrdersAdmin)