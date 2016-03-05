from django.contrib import admin

from .models import Payment, PaymentOrder


# class PaymentOrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'sum', 'created_at')

class PaymentAmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('status',)

admin.site.register(Payment, PaymentAmin)
# admin.site.register(PaymentOrder, PaymentOrderAdmin)
