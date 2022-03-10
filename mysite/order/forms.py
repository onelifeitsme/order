from django import forms
from django.forms import fields, models, formsets, widgets
from django.contrib.admin.widgets import AdminTextInputWidget, AdminIntegerFieldWidget
from django.conf import settings
from .models import Order, Product



class DateInput(forms.DateInput):
    input_type = 'date'


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('type', 'product', 'date', 'attachment',)
        widgets = {'date': DateInput(), 'address': forms.HiddenInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.none()

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['product'].queryset = Product.objects.filter(type_id=type_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['product'].queryset = self.instance.type.product_set.order_by('name')


class AddressForm(forms.Form):
    city = fields.CharField(max_length=150, label='display name', required=True)
    street = fields.CharField(widget=AdminTextInputWidget, required=True)
    house = fields.IntegerField(widget=AdminIntegerFieldWidget, required=True)
    apartment = fields.IntegerField(widget=AdminIntegerFieldWidget, required=True)

    def _get_media(self):
        media = widgets.Media(
            js=('%sjs/core.js' % settings.ADMIN_MEDIA_PREFIX,)
        )
        media += super(AddressForm, self).media
        return media
    media = property(_get_media)

AddressFormset = formsets.formset_factory(AddressForm, extra=1)
