from django.contrib import admin

from .forms import *


class BrowseAdmin(admin.ModelAdmin):
    form = BrowseForm


class ContactAdmin(admin.ModelAdmin):
    form = ContactForm

class TopicListingAdmin(admin.ModelAdmin):
    form = TopicListingForm


admin.site.register(Contact, ContactAdmin)
admin.site.register(Browse, BrowseAdmin)
admin.site.register(TopicListing, TopicListingAdmin)
