from django import forms

from .models import Generator, Payment


class GeneratorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields.get(field_name).widget.attrs = {
                'class' : 'form-control'
            }

    class Meta:
        model = Generator
        fields = ['quantity','serial','validity_time']


class PaymentForm(forms.ModelForm):


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields.get(field_name).widget.attrs = {
                'class' : 'form-control'
            }
    
    class Meta:
        model = Payment
        fields = ['price', 'card', 'comment']


    def clean(self) :
        
        data = self.cleaned_data
        card = data.get('card')
        price = data.get('price')

        if not card.status == card.ACTIVE:
            raise forms.ValidationError('This card is %s' %(card.status.lower()))

        else:
            if not card.amount >= price:
                raise forms.ValidationError('Insufficient amount')

        return data