
from django import forms
from home.models import *
from django.contrib.auth.models import User
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'  # O puedes especificar los campos que quieres mostrar en el formulario manualmente
 
class VentaForm(forms.ModelForm):
    cantidad = forms.IntegerField(min_value=1, label='Cantidad')
    total = forms.DecimalField(decimal_places=2, label='Total', disabled=True)

    class Meta:
        model = Venta
        fields = ['tipo_producto', 'Producto', 'cantidad', 'total']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Producto'].queryset = Producto.objects.all()
        self.fields['total'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get('cantidad')
        if cantidad is not None:
            producto = cleaned_data.get('Producto')
            if producto:
                precio_venta = producto.precio
                total = cantidad * precio_venta
                cleaned_data['total'] = total
                self.instance.total = total
        return cleaned_data