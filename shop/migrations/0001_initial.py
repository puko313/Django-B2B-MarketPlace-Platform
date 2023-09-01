# Generated by Django 2.0.2 on 2018-02-17 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('personInCharge', models.CharField(blank=True, default='', max_length=250)),
                ('shipAddress', models.CharField(blank=True, default='', max_length=250)),
                ('comment', models.TextField(blank=True, default='')),
                ('taxes', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('cancelled', models.BooleanField(default=False)),
                ('sale', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50)),
                ('invoice', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='shop.Invoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['datetime'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', related_query_name='items', to='shop.Order')),
            ],
            options={
                'verbose_name': 'OrderItem',
                'verbose_name_plural': 'OrderItems',
                'ordering': ['product'],
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(blank=True, default='', max_length=20)),
                ('kpp', models.CharField(blank=True, default='', max_length=20)),
                ('address', models.CharField(blank=True, default='', max_length=250)),
                ('name', models.CharField(blank=True, default='', max_length=250)),
                ('owners', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Organisation',
                'verbose_name_plural': 'Organisations',
                'ordering': ['inn'],
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50)),
                ('quantity', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'verbose_name': 'Price',
                'verbose_name_plural': 'Prices',
                'ordering': ['productVar', 'quantity'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(blank=True, default='')),
                ('priority', models.IntegerField(blank=True, default=0)),
                ('measure', models.CharField(blank=True, default='шт', max_length=50)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['priority', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ProductClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('priority', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'verbose_name': 'ProductClass',
                'verbose_name_plural': 'ProductClasses',
                'ordering': ['priority', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('addition', models.CharField(default='', max_length=140)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('priority', models.IntegerField(blank=True, default=0)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('vendorCode', models.CharField(blank=True, default=0, max_length=50)),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
            options={
                'verbose_name': 'ProductVariant',
                'verbose_name_plural': 'ProductVariants',
                'ordering': ['priority', 'name'],
            },
        ),
        migrations.CreateModel(
            name='SaleQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('sale', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50)),
                ('startQuantity', models.IntegerField(blank=True, default=0)),
                ('customers', models.ManyToManyField(blank=True, to='auth.Group')),
                ('productClasses', models.ManyToManyField(blank=True, to='shop.ProductClass')),
            ],
            options={
                'verbose_name': 'SaleQuantity',
                'verbose_name_plural': 'SalesQuantity',
                'ordering': ['sale', 'name'],
            },
        ),
        migrations.CreateModel(
            name='SaleSum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('sale', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50)),
                ('startSum', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50)),
                ('customers', models.ManyToManyField(blank=True, to='auth.Group')),
                ('productClasses', models.ManyToManyField(blank=True, to='shop.ProductClass')),
            ],
            options={
                'verbose_name': 'SaleSum',
                'verbose_name_plural': 'SalesSum',
                'ordering': ['sale', 'name'],
            },
        ),
        migrations.CreateModel(
            name='SellerOrganisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(blank=True, default='', max_length=20)),
                ('kpp', models.CharField(blank=True, default='', max_length=20)),
                ('address', models.CharField(blank=True, default='', max_length=250)),
                ('name', models.CharField(blank=True, default='', max_length=250)),
                ('bik', models.CharField(blank=True, default='', max_length=50)),
                ('corAcc', models.CharField(blank=True, default='', max_length=250)),
                ('bank', models.CharField(blank=True, default='', max_length=250)),
                ('checkACC', models.CharField(blank=True, default='', max_length=50)),
                ('owners', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SellerOrganisation',
                'verbose_name_plural': 'SellerOrganisations',
                'ordering': ['inn'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='productClass',
            field=models.ManyToManyField(blank=True, to='shop.ProductClass'),
        ),
        migrations.AddField(
            model_name='price',
            name='productVar',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='shop.ProductVariant'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ProductVariant'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Organisation'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shop.SellerOrganisation'),
        ),
    ]