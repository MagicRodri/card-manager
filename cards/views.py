from django.http import HttpResponse
from django.shortcuts import render

from .forms import GeneratorForm
from .models import Card

# Create your views here.

def card_list(request):
    """
    """
    cards = Card.objects.all()

    context = {
        'cards' : cards
    }
    return render(request,'cards/card_list.html', context=context)


def generator_create(request):
    """
    """

    generator_form = GeneratorForm()

    if request.method == 'POST':
        generator_form = GeneratorForm(data=request.POST)

        if generator_form.is_valid():
            generator_form.save()
            return HttpResponse('Generator created successfully')
    
    context = {
        'form' : generator_form
    }
    return render(request,'cards/generator_create.html',context=context)