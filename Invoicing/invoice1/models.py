from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User
from django.urls import reverse


class Client(models.Model):

    PROVINCES = [
    ('MadhyaPradesh', 'MadhyaPradesh'),
    ('Rajasthan', 'Rajasthan'),
    ('Maharashtra', 'Maharashtra'),
    ]

    #Basic Fields
    clientName = models.CharField(null=True, blank=True, max_length=200)
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    ClientLogo = models.ImageField(default='default_logo.jpg',upload_to='company_logos')
    province = models.CharField(choices=PROVINCES, blank=True, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=10)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)
    taxNumber = models.CharField(null=True, blank=True, max_length=100)


    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {} {}'.format(self.clientName, self.province, self.uniqueId)


    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)




class Invoice(models.Model):
    STATUS = [('CURRENT','CURRENT'),
              ('OVERDUE','OVERDUE'),
              ('PAID','PAID'),
              ('EMAIL-SENT!!','EMAIL-SENT!!')
              ]


    Title = models.CharField(null=True, blank=True, max_length=100)
    Number = models.CharField(null=True, blank=True, max_length=100)
    DueDate = models.DateField(null=True,blank=True)
    Status = models.CharField(choices=STATUS,default='CURRENT',max_length=100)
    Notes = models.TextField(null=True,blank=True)

    #related fields
    client = models.ForeignKey(Client, null=True, blank=True ,on_delete=models.SET_NULL)
    

    #utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.Number, self.uniqueId)


    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[1]
            # self.slug = slugify()
            self.slug = slugify('{} {}'.format(self.Number, self.uniqueId))

        # self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Invoice, self).save(*args, **kwargs)

class Product(models.Model):
    CURRENCY = [
    ('₹', 'INR'),
    ('$', 'USD'),
    ]

    title = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(choices=CURRENCY, default='₹', max_length=100)

    #related fields
    invoice = models.ForeignKey(Invoice, blank=True, null=True, on_delete=models.CASCADE)

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[1]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Product, self).save(*args, **kwargs)



class Settings(models.Model):

    PROVINCES = [
        ('MadhyaPradesh', 'MadhyaPradesh'),
        ('Rajasthan', 'Rajasthan'),
        ('Maharashtra', 'Maharashtra'),
        ]

    #Basic Fields
    clientName = models.CharField(null=True, blank=True, max_length=200)
    clientLogo = models.ImageField(default='default_logo.jpg', upload_to='company_logos')
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    province = models.CharField(choices=PROVINCES, blank=True, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=10)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)
    taxNumber = models.CharField(null=True, blank=True, max_length=100)


    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {} {}'.format(self.clientName, self.province, self.uniqueId)


    def get_absolute_url(self):
        return reverse('settings-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[1]
            self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Settings, self).save(*args, **kwargs)


    
    




