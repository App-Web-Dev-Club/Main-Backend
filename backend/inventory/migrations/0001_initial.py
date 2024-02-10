# Generated by Django 5.0.2 on 2024-02-10 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kids', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('damaged', 'Damaged'), ('avaliable', 'Avaliable'), ('taken', 'Taken')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_of_return', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taken_date', models.DateField()),
                ('expected_return_date', models.DateField()),
                ('actual_return_date', models.DateField()),
                ('permission_status', models.CharField(choices=[('rejected', 'Rejected'), ('accepted', 'Accepted'), ('hold', 'Hold')], max_length=100)),
                ('product_given', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kids.kh_club_members')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]
