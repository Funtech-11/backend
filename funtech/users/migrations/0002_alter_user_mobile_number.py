# Generated by Django 4.1.7 on 2024-04-28 08:23

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(max_length=20, null=True, validators=[users.validators.mobile_number_validator]),
        ),
    ]