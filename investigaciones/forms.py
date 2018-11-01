from django import forms
from .models import investigacion, categoria_investigacion

class estilo_investigacion(forms.ModelForm):
    class Meta:
        modelo = investigacion
        campo = ["titulo", "sinopsis"]

class formato_categoria(forms.Form):
    categorias = [
        (None, 'Selecciona una categoria')
    ]

    for categoria_inve in categoria_investigacion.objects.all():
        categorias.append((categoria_inve.name, categoria_inve.name))

    titulo = forms.CharField(max_length=200)
    sinopsis = forms.CharField(widget=forms.Textarea)
    categoria = forms.ChoiceField(widget=forms.Select(
        attrs={
            "class": "browser-default",
        }
    ), choices=categorias)
    autor = forms.CharField(max_length=50)

