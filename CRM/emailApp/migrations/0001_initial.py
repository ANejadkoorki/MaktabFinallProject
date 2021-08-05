# Generated by Django 3.2.5 on 2021-08-05 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='Creation Time')),
                ('receiver_email_address', models.EmailField(max_length=254, verbose_name='Receiver Email Address')),
                ('is_successful', models.BooleanField(default=False)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Expert')),
            ],
        ),
    ]
