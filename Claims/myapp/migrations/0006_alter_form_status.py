# Generated by Django 3.2.4 on 2021-07-04 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_form_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='status',
            field=models.CharField(blank=True, choices=[('IN_PROGRESS', 'In Progress'), ('ACCEPTED', 'Accepted')], max_length=15, null=True),
        ),
    ]