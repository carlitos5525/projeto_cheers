# Generated by Django 4.1.7 on 2023-03-08 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets_app', '0002_ticket_event_name_ticket_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='creation_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='description',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='ticket',
            name='is_sold',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='ticket',
            name='sales_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]