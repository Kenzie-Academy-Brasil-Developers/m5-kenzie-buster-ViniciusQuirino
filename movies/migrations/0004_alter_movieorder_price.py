# Generated by Django 4.1.7 on 2023-02-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0003_movieorder"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movieorder",
            name="price",
            field=models.FloatField(),
        ),
    ]
