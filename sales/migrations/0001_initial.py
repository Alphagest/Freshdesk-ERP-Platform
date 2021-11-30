# Generated by Django 3.2.5 on 2021-11-30 13:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0006_auto_20211130_1651'),
        ('products', '0002_alter_product_product_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date', models.DateField()),
                ('payment_type', models.CharField(choices=[('cash payment', 'Cash Payment'), ('credit payment', 'Credit Payment'), ('check payment', 'Check payment'), ('bank payment', 'Bank Payment')], max_length=50)),
                ('invoice_number', models.CharField(max_length=10)),
                ('sale_discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_sale', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Shipping_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('net_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due', models.DecimalField(decimal_places=2, max_digits=10)),
                ('charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
