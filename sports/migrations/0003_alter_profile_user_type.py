# Generated by Django 5.0.1 on 2024-02-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_alter_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, default='player', max_length=100, null=True),
        ),
    ]
