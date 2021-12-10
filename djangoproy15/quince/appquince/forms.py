from django import forms
from .models import Productos


class LaForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)



class ProductosForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Productos

        # specify fields to be used
        fields = [
            "nombre",
            "precio",
            "codigo",
            "categoria",
            "estado",
            "imagen",
        ]


      
