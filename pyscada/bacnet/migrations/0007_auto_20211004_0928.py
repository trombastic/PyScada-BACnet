# Generated by Django 2.2.8 on 2021-10-04 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0080_variableproperty_last_modified'),
        ('bacnet', '0006_remove_bacnetvariable_bacnet_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bacnetdevice',
            name='device_id',
        ),
        migrations.RemoveField(
            model_name='bacnetdevice',
            name='mac',
        ),
        migrations.RemoveField(
            model_name='bacnetdevice',
            name='product_description',
        ),
        migrations.RemoveField(
            model_name='bacnetdevice',
            name='product_model_number',
        ),
        migrations.RemoveField(
            model_name='bacnetdevice',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='bacnetdevice',
            name='protocol',
        ),
        migrations.RemoveField(
            model_name='bacnetdevice',
            name='unit_id',
        ),
        migrations.RemoveField(
            model_name='bacnetdevice',
            name='vendor_id',
        ),
        migrations.RemoveField(
            model_name='bacnetdevice',
            name='vendor_name',
        ),
        migrations.AddField(
            model_name='bacnetdevice',
            name='bacnet_local_device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='remote_devices', to='pyscada.Device'),
        ),
        migrations.AddField(
            model_name='bacnetdevice',
            name='device_type',
            field=models.PositiveSmallIntegerField(default=0, help_text='Set a local bacnet device to discover remote BACNet devices on the network'),
        ),
        migrations.AddField(
            model_name='bacnetdevice',
            name='mask',
            field=models.PositiveSmallIntegerField(default=24, help_text='Network mask'),
        ),
    ]
