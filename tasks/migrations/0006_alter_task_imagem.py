# Generated by Django 4.2.1 on 2023-07-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0005_alter_task_imagem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to="static/imagem"),
        ),
    ]
