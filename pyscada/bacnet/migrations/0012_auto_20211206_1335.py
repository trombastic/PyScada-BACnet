# Generated by Django 2.2.8 on 2021-12-06 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bacnet', '0011_auto_20211116_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='bacnetdevice',
            name='remote_devices_discovered',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='bacnetdevice',
            name='bacnet_local_device',
            field=models.ForeignKey(blank=True, limit_choices_to={'bacnetdevice__device_type': 0, 'bacnetdevice__isnull': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bacnet_remote_devices', to='pyscada.Device'),
        ),
    ]
