# Generated by Django 4.0.5 on 2022-06-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messager', '0002_message_delete_command_client_is_present_client_port_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='is_present',
        ),
        migrations.AddField(
            model_name='client',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
