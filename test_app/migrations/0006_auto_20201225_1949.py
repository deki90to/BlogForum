# Generated by Django 3.1.2 on 2020-12-25 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date']},
        ),
    ]
