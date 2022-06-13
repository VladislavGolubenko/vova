from django.contrib import admin
from .models import Booking, Profile, Realty, Pictures


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_start', 'date_end', 'id_realty', 'id_user', 'date_creation', 'amount')
    list_display_links = ('id',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'passport', 'id_user')
    list_display_links = ('id',)


class RealtyAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'rooms', 'bedrooms', 'price', 'region', 'address')
    list_display_links = ('id',)


class PicturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_realty', 'image_link')
    list_display_links = ('id',)


admin.site.register(Booking, BookingAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Realty, RealtyAdmin)
admin.site.register(Pictures, PicturesAdmin)
