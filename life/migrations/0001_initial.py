# Generated by Django 2.2.6 on 2019-10-17 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(choices=[('d', 'Dairy'), ('qi', 'quick idea')], max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('bodyText', models.TextField()),
            ],
        ),
    ]
