from django.contrib import admin

from models import *


class TransportTypeAdmin(admin.ModelAdmin):
    list_display = ('ads_field', 'as_string')


admin.site.register(TransportType, TransportTypeAdmin)


class SaleAdmin(admin.ModelAdmin):
    list_display = ('begin', 'end', 'product', 'transport_type', 'price',
                    'shopping_cart_description')

admin.site.register(Sale, SaleAdmin)


class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'sale', 'expire', 'discount')

admin.site.register(PromoCode, PromoCodeAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('exposed_id', 'date', 'user', 'billing', 'promo_code',
                    'is_free')
    ordering = ['-date']
    search_fields = ('exposed_id', 'date', 'promo_code')
    list_filter = ('promo_code', 'date')

admin.site.register(Order, OrderAdmin)


class OrderSaleAdmin(admin.ModelAdmin):
    list_display = ('order', 'sale', 'delivery', 'message')
    ordering = ['-order__date']
    search_fields = ('order__pk', 'order__exposed_id', 'delivery__firstname',
                     'delivery__lastname')
    list_filter = ('sale',)

admin.site.register(OrderSale, OrderSaleAdmin)


class DeliveredProductAdmin(admin.ModelAdmin):
    list_display = ('order_sale', 'product')
    search_fields = ('order_sale__order__pk', 'order_sale__order__exposed_id')
    list_filter = ('product',)


admin.site.register(DeliveredProduct, DeliveredProductAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'address', 'additional',
                    'zip_code', 'city', 'phone', 'country')
    search_fields = ('firstname', 'lastname', 'email', 'city')
    list_filter = ('country',)


admin.site.register(Address, AddressAdmin)


class Be2billTransactionAdmin(admin.ModelAdmin):

    def get_order_date(transaction):
        return transaction.order.date

    list_display = ('order', 'operationtype', 'date_insert', get_order_date,
                    'execcode', 'message', 'amount', 'cardfullname',
                    'clientemail')
    search_fields = ('clientemail', 'order__exposed_id')
    ordering = ['-order__date', '-date_insert']
    list_filter = ['execcode', 'currency', 'order__date']

admin.site.register(Be2billTransaction, Be2billTransactionAdmin)


class PartnersSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('order', 'date', 'register')
    list_filter = ('register', 'date')

admin.site.register(PartnersSubscription, PartnersSubscriptionAdmin)
