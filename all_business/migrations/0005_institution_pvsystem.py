# Generated by Django 2.2 on 2019-04-09 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('all_business', '0004_auto_20190409_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='pvsystem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='all_business.PvSystem'),
        ),
    ]
