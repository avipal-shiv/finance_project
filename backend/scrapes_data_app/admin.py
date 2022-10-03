from django.contrib import admin

# Register your models here.

from scrapes_data_app.models import * 

class WebscrapeAdmin(admin.ModelAdmin):

    list_display = ('name','price', 'hour', 'twenty_hours','seven_days','market_cap','volume','circulating_supply')


admin.site.register(Webscrap,WebscrapeAdmin)
