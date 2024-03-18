from django.contrib import admin
from .models import customer,staff,products
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(customer, MemberAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(staff, MemberAdmin)

admin.site.register(products)