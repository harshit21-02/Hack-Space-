# Generated by Django 4.2 on 2023-04-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_submission_flag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submission",
            name="Github",
            field=models.URLField(verbose_name="github"),
        ),
        migrations.AlterField(
            model_name="submission",
            name="Hackathon_name",
            field=models.CharField(max_length=200, verbose_name="hackathonname"),
        ),
        migrations.AlterField(
            model_name="submission",
            name="Other",
            field=models.URLField(blank=True, verbose_name="others"),
        ),
        migrations.AlterField(
            model_name="submission",
            name="Summary",
            field=models.CharField(blank=True, max_length=500, verbose_name="summary"),
        ),
        migrations.AlterField(
            model_name="submission",
            name="Title",
            field=models.CharField(max_length=200, verbose_name="title"),
        ),
    ]
