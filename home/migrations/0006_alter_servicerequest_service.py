# Generated by Django 5.0 on 2024-03-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_servicerequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='service',
            field=models.CharField(choices=[('plumbing', 'Plumbing'), ('carpentry', 'Carpentry'), ('electricity', 'Electricity')], max_length=255),
        ),
    ]
