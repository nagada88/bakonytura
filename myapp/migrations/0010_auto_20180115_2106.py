# Generated by Django 2.0.1 on 2018-01-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20180115_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bejegyzes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tartalom', models.CharField(max_length=2050)),
                ('szerzo', models.CharField(max_length=50)),
                ('bejegyzesidopont', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Bejegyzes',
            },
        ),
        migrations.DeleteModel(
            name='Dreamreal',
        ),
    ]
