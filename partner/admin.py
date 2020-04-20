from django.contrib import admin
from .models import Partner, Store, Menu

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('username','loginPW','loginID','usernumber','usernumber2')

admin.site.register(Partner, PartnerAdmin)

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','contact','address','description')
admin.site.register(Store, StoreAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('store','image','name','price')
admin.site.register(Menu, MenuAdmin)
