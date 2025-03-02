# Generated by Django 3.2.25 on 2025-02-25 05:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransportOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('order_number', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
