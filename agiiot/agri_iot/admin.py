from django.contrib import admin

from .models import APIKey, UserDetails, UserDayCount, StoreData, pricingmodel

# Register your models here.

admin.site.register(APIKey)
admin.site.register(UserDetails)
admin.site.register(UserDayCount)
admin.site.register(StoreData)
admin.site.register(pricingmodel)