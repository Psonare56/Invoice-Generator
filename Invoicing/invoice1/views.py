from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import *
from .models import *
from .functions import *
from django.http import HttpResponse

from django.contrib.auth.models import User, auth
from random import randint
from uuid import uuid4

import pdfkit
from django.template.loader import get_template
import os





#Anonymous required
def anonymous_required(function=None, redirect_url=None):

   if not redirect_url:
       redirect_url = 'dashboard'

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous,
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator



def index(request):
    context = {}
    return render(request, 'invoice/index.html', context)




def login(request):
    context = {}
    if request.method == 'GET':
        form = UserLoginForm()
        context['form'] = form
        return render(request, 'invoice/login.html', context)

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            return redirect('dashboard')
        else:
            context['form'] = form
            messages.error(request, 'Invalid Credentials')
            return redirect('login')


    return render(request, 'invoice/login.html', context)




@login_required
def dashboard(request):
    clients = Client.objects.all().count()
    invoices = Invoice.objects.all().count()
    paidInvoices = Invoice.objects.filter(Status='PAID').count()


    context = {}
    context['clients'] = clients
    context['invoices'] = invoices
    context['paidInvoices'] = paidInvoices
    return render(request, 'invoice/dashboard.html', context)

@login_required
def invoices(request):
    context = {}
    return render(request, 'invoice/invoices.html', context)





@login_required
def products(request):
    context = {}
    products = Product.objects.all()
    context['products'] = products

    return render(request, 'invoice/products.html', context)



@login_required
def invoices(request):
    context = {}
    invoices = Invoice.objects.all()
    context['invoices'] = invoices

    return render(request, 'invoice/invoices.html', context)

        
@login_required
def clients(request):
    context = {}
    clients = Client.objects.all()
    context['clients'] = clients

    if request.method == 'GET':
        form = ClientForm()
        context['form'] = form
        return render(request, 'invoice/clients.html', context)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Client Added')
            return redirect('clients')
        else:
            messages.error(request, 'Problem processing your request')
            context['form'] = form  # Pass the form with errors back to the context

    return render(request, 'invoice/clients.html', context)


def settings(request):
    context = {}
    settings = Settings.objects.all()
    context['settings'] = settings

    if request.method == 'GET':
        form = SettingsForm()
        context['form'] = form
        return render(request, 'invoice/settings.html', context)
    
    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Setting Added')
            return redirect('settings')        
        else:
            messages.error(request, 'Problem processing your request')
            context['form'] = form 
    
    return render(request, 'invoice/settings.html', context)







@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

#------------------------------build_invoice----------------------------

def createInvoice(request):
    number = 'INV-'+ str(uuid4()).split('-')[1]
    NewInvoice = Invoice.objects.create(Number=number)
    NewInvoice.save()

    inv = Invoice.objects.get(Number=number)
    return redirect('create-build-invoice',slug=inv.slug)


def createBuildInvoice(request, slug):
    try:
        invoice = Invoice.objects.get(slug=slug)
    except Invoice.DoesNotExist:
        messages.error(request, 'Invoice not found.')
        return redirect('invoices')

    products = Product.objects.filter(invoice=invoice)

    if request.method == 'POST':
        prod_form = ProductForm(request.POST)
        inv_form = InvoiceForm(request.POST, instance=invoice)
        client_form = ClientSelectForm(request.POST, instance=invoice)

        if prod_form.is_valid():
            product = prod_form.save(commit=False)
            product.invoice = invoice
            product.save()
            messages.success(request, 'Invoice Product Added Successfully')
            return redirect('create-build-invoice', slug=slug)

        if inv_form.is_valid():
            inv_form.save()
            messages.success(request, 'Invoice updated successfully')
            return redirect('create-build-invoice', slug=slug)

        if client_form.is_valid():
            client_form.save()
            messages.success(request, 'Client added to invoice successfully')
            return redirect('create-build-invoice', slug=slug)

        messages.error(request, 'Problem processing your request')
    else:
        prod_form = ProductForm()
        inv_form = InvoiceForm(instance=invoice)
        client_form = ClientSelectForm(instance=invoice)

    context = {
        'invoice': invoice,
        'products': products,
        'prod_form': prod_form,
        'inv_form': inv_form,
        'client_form': client_form,
    }

    return render(request, 'invoice/create-invoice.html', context)

# def createBuildInvoice(request, slug):
#     try:
#         invoice = Invoice.objects.get(slug=slug)
#     except Invoice.DoesNotExist:
#         messages.error(request, 'Something went wrong')
#         return redirect('invoices')

#     products = Product.objects.filter(invoice=invoice)

#     context = {
#         'invoice': invoice,
#         'products': products,
#     }

#     if request.method == 'GET':
#         context['prod_form'] = ProductForm()
#         context['inv_form'] = InvoiceForm(instance=invoice)
#         context['client_form'] = ClientSelectForm(instance=invoice.client)
#         return render(request, 'invoice/create-invoice.html', context)

#     if request.method == 'POST':
#         prod_form = ProductForm(request.POST)
#         inv_form = InvoiceForm(request.POST, instance=invoice)
#         client_form = ClientSelectForm(request.POST, instance=invoice.client)

#         if prod_form.is_valid():
#             product = prod_form.save(commit=False)
#             product.invoice = invoice
#             product.save()
#             messages.success(request, 'Invoice Product Added Successfully')
#             return redirect('create-build-invoice', slug=slug)

#         if inv_form.is_valid():
#             inv_form.save()
#             messages.success(request, 'Invoice updated successfully')
#             return redirect('create-build-invoice', slug=slug)

#         if client_form.is_valid() and 'client' in request.POST:
#             client_form.save()
#             messages.success(request, 'Client added to invoice successfully')
#             return redirect('create-build-invoice', slug=slug)

#         context['prod_form'] = prod_form
#         context['inv_form'] = inv_form
#         context['client_form'] = client_form
#         messages.error(request, 'Problem processing your request')
#         return render(request, 'invoice/create-invoice.html', context)

#     return render(request, 'invoice/create-invoice.html', context)



# def createBuildInvoice(request, slug):
#     #fetch that invoice
#     try:
#         invoice = Invoice.objects.get(slug = slug)
#         pass
#     except:
#         messages.error(request, 'Something Went Wrong')
#         return redirect('invoices')
    
#     #fetch all the products
#     products = Product.objects.filter(invoice=invoice)

#     context = {}
#     context['invoice'] = invoice
#     context['products'] = products

#     if request.method == 'GET':
#         prod_form = ProductForm()
#         inv_form = InvoiceForm(instance=invoice)
#         client_form = ClientSelectForm(initial_client=Invoice.client)
       
#         context['prod_form'] = prod_form
#         context['inv_form'] = inv_form
#         context['client_form'] = client_form
        
#         return render(request, 'invoice/create-invoice.html', context)
    
#     if request.method == 'POST':
#         prod_form = ProductForm(request.POST)
#         inv_form = InvoiceForm(request.POST,instance=invoice)
#         client_form = ClientSelectForm(request.POST,initial_client=Invoice.client)

#         if prod_form.is_valid():
#             obj = prod_form.save(commit=False)
#             obj.invoice = invoice
#             obj.save()

#             messages.success(request, 'Invoice Product Added Successfully')
#             return redirect('create-build-invoice',slug=slug)
        
#         elif inv_form.is_valid():
#             inv_form.save()

#             messages.success(request, "Invoice updated succesfully")
#             return redirect('create-build-invoice', slug=slug)
#         elif client_form.is_valid() and 'client' in request.POST:

#             client_form.save()
#             messages.success(request, "Client added to invoice succesfully")
#             return redirect('create-build-invoice', slug=slug)
        
#         else:
#             context['prod_form'] = prod_form
#             context['inv_form'] = inv_form
#             context['client_form'] = client_form
#             messages.error(request,"Problem processing your request")
#             return render(request, 'invoice/create-invoice.html', context)
        
#     return render(request, 'invoice/create-invoice.html', context)


def viewDocumentInvoice(request, slug):
    #fetch that invoice
    try:
        invoice = Invoice.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    #fetch all the products - related to this invoice
    products = Product.objects.filter(invoice=invoice)

    #Get Client Settings
    p_settings = Settings.objects.get(clientName='OnlineStiches')

    #Calculate the Invoice Total
    invoiceTotal = 0.0
    if len(products) > 0:
        for x in products:
            y = float(x.quantity) * float(x.price)
            invoiceTotal += y



    context = {}
    context['invoice'] = invoice
    context['products'] = products
    context['p_settings'] = p_settings
    context['invoiceTotal'] = "{:.2f}".format(invoiceTotal)

    #The name of your PDF file
    filename = '{}.pdf'.format(invoice.uniqueId)

    #HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('invoice/pdf-template.html')


    #Render the HTML
    html = template.render(context)

    #Options - Very Important [Don't forget this]
    options = {
          'encoding': 'UTF-8',
          'javascript-delay':'10', #Optional
          'enable-local-file-access': None, #To be able to access CSS
          'page-size': 'A4',
          'custom-header' : [
              ('Accept-Encoding', 'gzip')
          ],
      }
      #Javascript delay is optional

    #Remember that location to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    #IF you have CSS to add to template
    # css1 = os.path.join(settings.CSS_LOCATION, 'assets', 'css', 'bootstrap.min.css')
    # css2 = os.path.join(settings.CSS_LOCATION, 'assets', 'css', 'dashboard.css')

    #Create the file
    file_content = pdfkit.from_string(html, False, configuration=config, options=options)

    #Create the HTTP Response
    response = HttpResponse(file_content, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename = {}'.format(filename)

    #Return
    return response

def viewPDFInvoice(request, slug):
    #fetch that invoice
    try:
        invoice = Invoice.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    #fetch all the products - related to this invoice
    products = Product.objects.filter(invoice=invoice)

    #Get Client Settings
    p_settings = Settings.objects.get(clientName='OnlineStiches')

    #Calculate the Invoice Total
    invoiceCurrency = ''
    invoiceTotal = 0.0
    if len(products) > 0:
        for x in products:
            y = float(x.quantity) * float(x.price)
            invoiceTotal += y
            invoiceCurrency = x.currency



    context = {}
    context['invoice'] = invoice
    context['products'] = products
    context['p_settings'] = p_settings
    context['invoiceTotal'] = "{:.2f}".format(invoiceTotal)
    context['invoiceCurrency'] = invoiceCurrency

    return render(request, 'invoice/invoice-template.html', context)


def emailDocumentInvoice(request, slug):
    #fetch that invoice
    try:
        invoice = Invoice.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    #fetch all the products - related to this invoice
    products = Product.objects.filter(invoice=invoice)

    #Get Client Settings
    p_settings = Settings.objects.get(clientName='OnlineStiches')

    #Calculate the Invoice Total
    invoiceTotal = 0.0
    if len(products) > 0:
        for x in products:
            y = float(x.quantity) * float(x.price)
            invoiceTotal += y



    context = {}
    context['invoice'] = invoice
    context['products'] = products
    context['p_settings'] = p_settings
    context['invoiceTotal'] = "{:.2f}".format(invoiceTotal)

    #The name of your PDF file
    filename = '{}.pdf'.format(invoice.uniqueId)

    #HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('invoice/pdf-template.html')


    #Render the HTML
    html = template.render(context)

    options = {
          'encoding': 'UTF-8',
          'javascript-delay':'100', #Optional
          'enable-local-file-access': None, #To be able to access CSS
          'page-size': 'A4',
          'custom-header' : [
              ('Accept-Encoding', 'gzip')
          ],
      }
    

    #Remember that location to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=r'/usr/bin/wkhtmltopdf')

    #Saving the File
    filepath = os.path.join(settings.MEDIA_ROOT, 'client_invoices')
    os.makedirs(filepath, exist_ok=True)
    pdf_save_path = filepath+filename
    #Save the PDF
    pdfkit.from_string(html, pdf_save_path, configuration=config, options=options)


    #send the emails to client
    to_email = invoice.client.emailAddress
    from_client = p_settings.clientName
    emailInvoiceClient(to_email, from_client, pdf_save_path)

    invoice.status = 'EMAIL_SENT'
    invoice.save()

    #Email was send, redirect back to view - invoice
    messages.success(request, "Email sent to the client succesfully")
    return redirect('create-build-invoice', slug=slug)


def deleteInvoice(request, slug):
    try:
        Invoice.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    return redirect('invoices')


def companySettings(request):
    company = Settings.objects.get(clientName='OnlineStiches')
    context = {'company': company}
    return render(request, 'invoice/company-settings.html', context)


    
    

    