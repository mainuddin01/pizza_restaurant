from django.shortcuts import render
from django.views import generic
from . models import MainSlider, Greeting, GreetingItem, CallToAction
from dishes.models import Dish

# Create your views here.
class HomeView(generic.View):
    def get(self, request, *args, **kwargs):
        context = {
            'greeting_obj': Greeting.objects.first(),
            'dishes': Dish.objects.all(),
            'cta': CallToAction.objects.first(),
        }
        return render(request, 'index.html', context)
