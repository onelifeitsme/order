from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import CreateView
from .forms import OrderForm, ContactFormset, EventFormset


class OrderView(CreateView):
    template_name = 'order/order.html'
    form_class = OrderForm
    success_url = '/'


def display_data(request, data, **kwargs):
    return render('example/posted-data.html', dict(data=data, **kwargs),
        context_instance=RequestContext(request))


def multiple_formsets(request):
    if request.method == 'POST':
        contact_formset, event_formset = ContactFormset(request.POST, prefix='contact_form'), EventFormset(request.POST, prefix='event_form')
        if contact_formset.is_valid() and event_formset.is_valid():
            data = [contact_formset.cleaned_data, event_formset.cleaned_data]
            return display_data(request, data, multiple_formsets=True)
    else:
        contact_formset, event_formset = ContactFormset(prefix='contact_form'), EventFormset(prefix='event_form')
    return render(request, 'order/order.html', {'contact_formset': contact_formset, 'event_formset': event_formset})

