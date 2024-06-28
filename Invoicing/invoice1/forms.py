from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *
import json

#Form Layout from Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class DateInput(forms.DateInput):
    input_type = 'date'

class UserLoginForm(forms.ModelForm):
    username = forms.CharField(
                            widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
                            required=True)
    password = forms.CharField(
                            widget=forms.PasswordInput(attrs={'id': 'floatingPassword', 'class': 'form-control mb-3'}),
                            required=True)


    class Meta:
        model=User
        fields=['username','password']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'clientName', 
            'addressLine1', 
            'province', 
            'postalCode', 
            'phoneNumber', 
            'emailAddress', 
            'taxNumber'
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'quantity', 'price', 'currency']


class InvoiceForm(forms.ModelForm):

    STATUS_OPTIONS = [
    ('CURRENT', 'CURRENT'),
    ('OVERDUE', 'OVERDUE'),
    ('PAID', 'PAID'),
    ]

    Title = forms.CharField(
                    required = True,
                    label='Invoice Name or Title',
                    widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Invoice Title'}),)
    Status = forms.ChoiceField(
                    choices = STATUS_OPTIONS,
                    required = True,
                    label='Change Invoice Status',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    Notes = forms.CharField(
                    required = True,
                    label='Enter any notes for the client',
                    widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))

    DueDate = forms.DateField(
                        required = True,
                        label='Invoice Due',
                        widget=DateInput(attrs={'class': 'form-control mb-3'}),)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('Title', css_class='form-group col-md-6'),
                Column('DueDate', css_class='form-group col-md-6'),
                css_class='form-row'),
            Row(
                Column('Status', css_class='form-group col-md-6'),
                css_class='form-row'),
            'Notes',

            Submit('submit', ' EDIT INVOICE '))

    class Meta:
        model = Invoice
        fields = ['Title', 'DueDate', 'Status', 'Notes']



class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['clientName', 'clientLogo', 'addressLine1', 'province', 'postalCode', 'phoneNumber', 'emailAddress', 'taxNumber']




# class ClientSelectForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         # Use `get` method to avoid `KeyError` if `initial_client` is not provided
#         self.initial_client = kwargs.pop('initial_client', None)
#         self.CLIENT_LIST = Client.objects.all()
#         self.CLIENT_CHOICES = [('-----', '--Select a Client--')]

#         for client in self.CLIENT_LIST:
#             d_t = (client.uniqueId, client.clientName)
#             self.CLIENT_CHOICES.append(d_t)

#         super(ClientSelectForm, self).__init__(*args, **kwargs)

#         self.fields['client'] = forms.ChoiceField(
#             label='Choose a related client',
#             choices=self.CLIENT_CHOICES,
#             widget=forms.Select(attrs={'class': 'form-control mb-3'}),
#         )

#     class Meta:
#         model = Invoice
#         fields = ['client']

#     def clean_client(self):
#         c_client = self.cleaned_data['client']
#         if c_client == '-----':
#             return self.initial_client
#         else:
#             return Client.objects.get(uniqueId=c_client)


class ClientSelectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.initial_client = kwargs.pop('initial_client', None)
        super(ClientSelectForm, self).__init__(*args, **kwargs)

        self.CLIENT_CHOICES = [('-----', '--Select a Client--')] + [
            (client.uniqueId, client.clientName) for client in Client.objects.all()
        ]

        self.fields['client'] = forms.ChoiceField(
            label='Choose a related client',
            choices=self.CLIENT_CHOICES,
            widget=forms.Select(attrs={'class': 'form-control mb-3'}),
        )

    class Meta:
        model = Invoice
        fields = ['client']

    def clean_client(self):
        c_client = self.cleaned_data['client']
        if c_client == '-----':
            return self.initial_client
        try:
            return Client.objects.get(uniqueId=c_client)
        except Client.DoesNotExist:
            raise forms.ValidationError("Selected client does not exist.")