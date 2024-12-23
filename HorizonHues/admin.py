from django.contrib import admin
from .models import *

class TouristAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'phone_number', 'date')
    list_display_links = ('fname','email',)

admin.site.register(Tourist, TouristAdmin)

class PackageAdmin(admin.ModelAdmin):
    list_display = ('package_id', 'location','group', 'prev_price', 'discount','discounted_price','nights','days')
    list_display_links = ('package_id','location',)

admin.site.register(Package, PackageAdmin)

class Buy_nowAdmin(admin.ModelAdmin):
    list_display = ('package_id', 'location')
    list_display_links = ('package_id','location')

admin.site.register(Buy_now, Buy_nowAdmin)
    
class MyCartAdmin(admin.ModelAdmin):
    list_display = ('cart_id','email','package_id', 'location','group', 'prev_price', 'discount','discounted_price','nights','days')
    list_display_links = ('cart_id','email','package_id','location',)

admin.site.register(MyCart, MyCartAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email' ,'phone', 'review', 'suggestion')
    list_display_links = ('name','email')

admin.site.register(Feedback, FeedbackAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','fname','email','package_id', 'location','checkin_date','checkout_date')
    list_display_links = ('order_id','email','package_id')

admin.site.register(Order, OrderAdmin)

admin.site.register(Home)

class HotelAdmin(admin.ModelAdmin):
    list_display = ('Hotel_id', 'location','group', 'prev_price', 'discount','discounted_price')
    list_display_links = ('Hotel_id','location',)
admin.site.register(Hotel, HotelAdmin)