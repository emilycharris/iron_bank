from django.contrib import admin
from bank.models import Transaction

# Register your models here.

class AdminView(admin.ModelAdmin):
    list_display = ('user', 'dollar_amount', 'vendor', 'date', 'transaction_type')


admin.site.register(Transaction, AdminView)
