# Generated by Django 5.0.1 on 2024-03-09 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0002_jobdetails_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobdetails',
            old_name='benifits',
            new_name='benefits',
        ),
    ]
