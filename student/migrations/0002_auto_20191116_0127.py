# Generated by Django 2.1 on 2019-11-15 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='books_issued',
            field=models.ManyToManyField(blank=True, null=True, to='books.book'),
        ),
    ]
