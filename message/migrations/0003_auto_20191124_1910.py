# Generated by Django 2.2.7 on 2019-11-24 15:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0002_auto_20191106_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversations',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ConversationMembers',
        ),
    ]
