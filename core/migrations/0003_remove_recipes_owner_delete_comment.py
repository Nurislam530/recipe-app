# Generated by Django 4.2.5 on 2023-10-06 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipes_owner_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]