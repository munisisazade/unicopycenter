from django.contrib import admin
from center.models import Orders, Uploads
# Register your models here.
class UploadsInline(admin.TabularInline):
    model = Uploads
    extra = 5


class OrdersAdmin(admin.ModelAdmin):
    inlines = [UploadsInline, ]
    list_display = ('full_name', 'number', 'email','date')
    list_filter = ('date',)
    search_fields = ('full_name',)
    fieldsets = [
        ('Sifarışçi haqqında ətraflı məlumat', {
            'fields': ['full_name', 'universitet', 'kurs','group']
        }),
        ('Elaqə üçün məlumatlar', {
            'fields': ['email', 'number']
        }),
        ('İcra olunmalıdır', {
            'fields': ['types','text','date']
        }),
    ]

class UploadsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['upload_file', 'file']
        }),
    ]

admin.site.register(Orders,OrdersAdmin)
admin.site.register(Uploads,UploadsAdmin)