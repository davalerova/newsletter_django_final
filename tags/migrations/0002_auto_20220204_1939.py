# Generated by Django 3.2 on 2022-02-04 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='update_add',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='date_created',
            new_name='update_at',
        ),
    ]