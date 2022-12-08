from django.http import HttpResponse
from django.shortcuts import render

from .forms import GeneratorForm, PaymentForm
from .models import Card

# Create your views here.

def card_list(request):
    """
    """
    cards = Card.objects.all()
    q = request.GET.get('q')
    if q:
        cards = cards.search(q)
    context = {
        'cards' : cards
    }
    return render(request,'cards/card_list.html', context=context)

def card_history(request, pk):

    return render(request,'cards/card_history.html')

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


def payment_create(request):
    """
    """

    payment_form = PaymentForm()

    if request.method == 'POST':
        payment_form = PaymentForm(data=request.POST)

        if payment_form.is_valid():
            payment_form.save()
            return HttpResponse('Payment created successfully')
    
    context = {
        'form' : payment_form
    }
    return render(request,'cards/payment_create.html',context=context)