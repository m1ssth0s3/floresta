# Generated by Django 4.2.7 on 2023-11-24 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_product_total_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=8, null=True),
        ),
    ]
