# Generated by Django 5.1 on 2024-10-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('Vegetable', 'Vegetable'), ('Fruit', 'Fruit'), ('Others', 'Others')])),
                ('calories', models.FloatField()),
                ('seasonal', models.BooleanField()),
                ('image', models.CharField(null=True)),
            ],
        ),
    ]
