# Generated by Django 5.2.1 on 2025-05-11 12:24

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingLot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=300)),
                ('address', models.TextField()),
                ('pin_code', models.CharField(max_length=10)),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('total_spaces', models.PositiveBigIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('space_number', models.CharField(max_length=10)),
                ('floor', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(choices=[('A', 'Available'), ('O', 'Occupied'), ('R', 'Reserved'), ('M', 'Maintenance')], default='A', max_length=1)),
                ('is_accessible', models.BooleanField(default=False, help_text='Space designed for accessibility needs')),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parking_lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spaces', to='parking.parkinglot')),
            ],
            options={
                'unique_together': {('parking_lot', 'space_number')},
            },
        ),
    ]
