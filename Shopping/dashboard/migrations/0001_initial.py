# Generated by Django 4.0.4 on 2022-04-28 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mehsullar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mehsullar.category')),
            ],
            bases=('mehsullar.category',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mehsullar.product')),
            ],
            bases=('mehsullar.product',),
        ),
    ]
