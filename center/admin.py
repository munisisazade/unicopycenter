from django.contrib import admin
from center.models import Orders, Uploads
# Register your models here.
class UploadsInline(admin.TabularInline):
    model = Uploads
    extra = 4
    readonly_fields = ('upload_file','file','fayl_name')
    raw_id_fields = ('relation',)
    exclude = ('upload_file',)
    fieldsets = [
        ('İcra olunmalıdır', {
            'fields': ['upload_file','file', 'fayl_name']
        }),
    ]



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
    #readonly_fields = ('upload_file',)
    #list_display = ('relation','file','upload_file')
    # fieldsets = [
    #     ('İcra olunmalıdır', {
    #         'fields': ['relation','upload_file','file']
    #     }),
    # ]
    pass

admin.site.register(Orders,OrdersAdmin)
#admin.site.register(Uploads,UploadsAdmin)