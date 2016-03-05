from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from invoices.translation import InvoiceTranslationOptions
from .models import Invoice

class InvoiceAdmin(TabbedTranslationAdmin):
    list_display = ('__unicode__', 'user', 'status', 'price', 'updated_at', 'created_at')
    list_display_links = ('__unicode__', 'user',)
    readonly_fields = ('status',)
    formfield_overrides = {}

admin.site.register(Invoice, InvoiceAdmin)