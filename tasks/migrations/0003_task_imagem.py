# Generated by Django 4.2.1 on 2023-07-25 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_alter_task_done"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to="Task"),
        ),
    ]