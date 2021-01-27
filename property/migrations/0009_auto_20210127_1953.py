# Generated by Django 2.2.4 on 2021-01-27 16:53
from django.db import migrations
import phonenumbers

def normalize_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        number = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(number):
            phone_number = phonenumbers.format_number(
                number,
                phonenumbers.PhoneNumberFormat.E164
            )
            flat.owner_pure_phone = phone_number
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20210126_2024'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_number),
    ]
