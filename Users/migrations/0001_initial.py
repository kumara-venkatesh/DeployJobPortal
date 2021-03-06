# Generated by Django 3.0.3 on 2020-05-20 08:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JSProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='default.jpg', upload_to='profile_pics/')),
                ('BirthDate', models.DateField()),
                ('phoneno', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\d+)*\\Z'), code='invalid', message=None), django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator('^\\d{0,10}$')])),
                ('address', models.CharField(max_length=100)),
                ('Qualification', models.CharField(blank=True, max_length=200)),
                ('Resume', models.FileField(upload_to='Files/')),
                ('Designation', models.CharField(blank=True, max_length=100)),
                ('Experience', models.IntegerField(blank=True)),
                ('CompanyName', models.CharField(blank=True, max_length=100)),
                ('Skills', models.CharField(blank=True, max_length=500)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
