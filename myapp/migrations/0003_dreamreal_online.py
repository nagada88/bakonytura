# Generated by Django 2.0.1 on 2018-01-14 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='dreamreal',
            name='online',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.Online'),
        ),
    ]
