# Generated by Django 2.1 on 2019-11-15 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
