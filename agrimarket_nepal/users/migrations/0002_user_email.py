# Generated by Django 5.1 on 2024-08-12 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=254, unique=True),
        ),
    ]