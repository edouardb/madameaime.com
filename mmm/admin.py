from django.contrib import admin

from models import *


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date', 'active')

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(OfferPage)
admin.site.register(OfferPageSale)
