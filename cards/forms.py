from django import forms

from .models import Generator


class GeneratorForm(forms.ModelForm):

    class Meta:
        model = Generator
        fields = ['quantity','serial','validity_time']