# Generated by Django 2.2.7 on 2019-11-06 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='token',
            field=models.UUIDField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivers', to='users.Users'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senders', to='users.Users'),
        ),
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='firstname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=1000),
        ),
    ]