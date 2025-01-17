from django.contrib import admin
from .models import Transaction, User, Balance



@admin.register(User)
class AppUsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined')
    search_fields = ('username',)
    list_filter = ('date_joined',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'transaction_type', 'description')
    search_fields = ('user',)
    list_filter = ('user', 'amount', 'transaction_type')


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('id',  'balance')
    search_fields = ('balance',)
    list_filter = ('balance',)