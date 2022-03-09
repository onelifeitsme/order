from django import forms
from django.forms import fields, models, formsets, widgets
from django.contrib.admin.widgets import AdminDateWidget
from django.conf import settings

from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


CONTACT_INFO_TYPES = (
    ('Phone', 'Phone'),
    ('Fax', 'Fax'),
    ('Email', 'Email'),
    ('AIM', 'AIM'),
    ('Gtalk', 'Gtalk/Jabber'),
    ('Yahoo', 'Yahoo'),
)

class ContactInfoForm(forms.Form):
    type = fields.ChoiceField(choices=CONTACT_INFO_TYPES)
    value = fields.CharField(max_length=200)
    preferred = fields.BooleanField(required=False)

ContactFormset = formsets.formset_factory(ContactInfoForm)
# Define a formset, which will allow a maximum of 5 contacts, no more:
MaxFiveContactsFormset = formsets.formset_factory(ContactInfoForm, extra=5, max_num=5)
# Define the same formset, with no forms (so we can demo the form template):
EmptyContactFormset = formsets.formset_factory(ContactInfoForm, extra=0)
try:
    # Define the same formset, which will require a minimum of 2 contacts, no extra
    MinTwoContactsFormset = formsets.formset_factory(ContactInfoForm, extra=0, min_num=2)
except:
    pass # django pre 1.7

###############################################
## Plain 'ole Formset with Javascript Widget ##
###############################################

class EventForm(forms.Form):
    name = fields.CharField(max_length=150, label='display name')
    start_date = fields.DateField(widget=AdminDateWidget)
    end_date = fields.DateField(widget=AdminDateWidget)

    def _get_media(self):
        # The "core.js" file is required by the Admin Date widget, yet for
        # some reason, isn't included in the widgets media definition.
        # We override "_get_media" because core.js needs to appear BEFORE
        # the widget's JS files, and the default order puts the form's
        # media AFTER that of its fields.
        media = widgets.Media(
            js=('%sjs/core.js' % settings.ADMIN_MEDIA_PREFIX,)
        )
        media += super(EventForm, self).media
        return media
    media = property(_get_media)

EventFormset = formsets.formset_factory(EventForm, extra=2)
