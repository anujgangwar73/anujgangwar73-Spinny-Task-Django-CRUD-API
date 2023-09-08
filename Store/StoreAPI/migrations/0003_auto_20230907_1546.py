# Generated by Django 3.2.21 on 2023-09-07 10:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('StoreAPI', '0002_auto_20230907_1449'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='box',
            name='total_boxes_added_in_a_week',
        ),
        migrations.AddConstraint(
            model_name='box',
            constraint=models.CheckConstraint(check=models.Q(('created_at__gte', datetime.datetime(2023, 8, 31, 10, 16, 53, 860499, tzinfo=utc))), name='total_boxes_added_in_a_week'),
        ),
    ]
