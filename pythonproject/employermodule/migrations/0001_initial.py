# Generated by Django 5.0.1 on 2024-01-31 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(max_length=225)),
                ('salary_offered', models.CharField(max_length=225)),
                ('job_type', models.CharField(choices=[('fulltime', 'Full-time'), ('parttime', 'Part-time'), ('contract', 'Contract')], max_length=20)),
                ('benifits', models.TextField()),
                ('education', models.CharField(max_length=225)),
                ('work_location', models.CharField(max_length=225)),
                ('required_skills', models.TextField()),
            ],
        ),
    ]
