# Generated by Django 4.1.7 on 2024-04-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userevent',
            name='qr_code',
            field=models.ImageField(max_length=50, null=True, upload_to='', verbose_name='QR код'),
        ),
    ]
