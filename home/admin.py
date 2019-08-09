from django.contrib import admin
from .models import MainSlider, Greeting, GreetingItem, CallToAction, Testimonial

# Register your models here.
class GreetingItemsInline(admin.StackedInline):
    model = GreetingItem
    extra = 1

class GreetingAdmin(admin.ModelAdmin):
    inlines = [GreetingItemsInline]

admin.site.register(MainSlider)
admin.site.register(Greeting, GreetingAdmin)
admin.site.register(GreetingItem)
admin.site.register(CallToAction)
admin.site.register(Testimonial)