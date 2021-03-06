# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='dollar_amount',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('DR', 'Debit'), ('CR', 'Credit')], default='DR', max_length=10),
        ),
    ]
