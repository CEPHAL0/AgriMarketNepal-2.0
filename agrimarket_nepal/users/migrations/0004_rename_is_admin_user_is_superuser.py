# Generated by Django 5.1 on 2024-08-12 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_is_admin_user_is_staff_alter_user_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_superuser',
        ),
    ]
