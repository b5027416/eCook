# Generated by Django 2.2 on 2019-04-22 15:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviewApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProdReview',
            new_name='Review',
        ),
    ]