# Generated by Django 4.1.3 on 2022-12-08 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FeedModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Feedback", models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="UserPredictDataModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gender", models.IntegerField()),
                ("age", models.IntegerField()),
                ("hypertension", models.IntegerField()),
                ("heart_disease", models.IntegerField()),
                ("avg_glucose_level", models.IntegerField()),
                ("bmi", models.IntegerField()),
                ("smoking_status", models.IntegerField()),
                ("stroke", models.IntegerField()),
            ],
        ),
    ]
