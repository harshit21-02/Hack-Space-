# Generated by Django 4.1.3 on 2023-04-22 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_submission_description_submission_github_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="flag",
            field=models.BooleanField(default=False, verbose_name="flag"),
            preserve_default=False,
        ),
    ]