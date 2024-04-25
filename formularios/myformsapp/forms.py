from django import forms
from .models import MyModel

class MyCustomForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['Nombre', 'Telefono', 'Motivo', 'Mensaje']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Mensaje'].widget = forms.Textarea(attrs={'rows': 4})
