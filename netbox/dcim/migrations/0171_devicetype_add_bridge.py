# Generated by Django 4.1.6 on 2023-03-01 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0170_configtemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='interfacetemplate',
            name='bridge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bridge_interfaces', to='dcim.interfacetemplate'),
        ),
    ]
