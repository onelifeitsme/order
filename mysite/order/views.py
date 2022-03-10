from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import Product, Order
from .forms import OrderForm, AddressFormset


class OrderView(CreateView):
    """Представление оформления заказа"""
    model = Order
    template_name = 'order/order.html'
    form_class = OrderForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address_formset'] = AddressFormset(prefix='address_form')
        return context

    def form_valid(self, form):
        address_formset = AddressFormset(self.request.POST, prefix='address_form')
        if address_formset.is_valid():
            addresses = ''
            for address in address_formset.cleaned_data:
                addresses += f'• Город {address["city"]}, улица/проспект {address["street"]}, ' \
                             f'{address["house"]}-{address["apartment"]}\n'
            form.instance.address = addresses
            current_order = form.save()
            print(self.request.POST)
            return render(self.request, 'order/order.html', {'current_order': current_order})
        else:
            print(form.cleaned_data)
            return render(self.request, 'order/order.html',
                          {'form': self.form_class(initial=form.cleaned_data),
                           'address_formset': AddressFormset(prefix='address_form'),
                           'address_error': 'Необходимо указать адрес'})


class LoadProducts(TemplateView):
    """Получение списка товаров, относящихся к конкретному типу"""
    template_name = 'order/product_dropdown_list_options.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_id'] = self.request.GET.get('type_id')
        context['products'] = Product.objects.filter(type_id=context['type_id']).all()
        return context
