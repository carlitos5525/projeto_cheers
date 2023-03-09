# Generated by Django 4.1.7 on 2023-03-09 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets_app', '0003_ticket_creation_date_ticket_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='creation_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='sales_date',
            new_name='sold_at',
        ),
    ]
