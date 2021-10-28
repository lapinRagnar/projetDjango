# Generated by Django 3.2.8 on 2021-10-25 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'Article'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='created_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]