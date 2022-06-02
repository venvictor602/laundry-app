from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name','last_name','address', 'date_of_appointment']
    list_display_links = ('first_name','last_name','address')
    search_fields = ('first_name','last_name','address')
    list_per_page = 25
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name','service_render','status']
    list_display_links = ('full_name','service_render')
    search_fields = ('full_name','service_render')
    list_per_page = 25

class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_income_for_today','total_profit_for_today', 'created_at']
    list_display_links = ('total_income_for_today','total_profit_for_today')
    search_fields = ('total_income_for_today','total_profit_for_today')
    list_per_page = 25

admin.site.register(Inventory)
admin.site.register(Report,ReportAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Employee,EmployeeAdmin)
