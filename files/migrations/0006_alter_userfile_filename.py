# Generated by Django 4.2.20 on 2025-04-19 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0005_delete_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userfile",
            name="filename",
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
