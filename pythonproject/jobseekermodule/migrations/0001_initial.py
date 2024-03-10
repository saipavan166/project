# Generated by Django 5.0.1 on 2024-02-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('tenth_marks', models.CharField(max_length=10)),
                ('twelth_marks', models.CharField(max_length=10)),
                ('cgpa', models.CharField(max_length=10)),
                ('expected_salary', models.CharField(max_length=10)),
                ('position', models.CharField(max_length=10)),
            ],
        ),
    ]
