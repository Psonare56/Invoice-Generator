# Generated by Django 5.0.6 on 2024-06-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='Status',
            field=models.CharField(choices=[('CURRENT', 'CURRENT'), ('OVERDUE', 'OVERDUE'), ('PAID', 'PAID'), ('EMAIL-SENT!!', 'EMAIL-SENT!!')], default='CURRENT', max_length=100),
        ),
    ]
