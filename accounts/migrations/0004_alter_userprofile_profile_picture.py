# Generated by Django 4.2 on 2023-04-26 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_userprofile_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(blank=True, upload_to="images/users/"),
        ),
    ]
