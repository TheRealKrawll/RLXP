# Generated by Django 4.0.2 on 2022-04-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rlxp', '0008_alter_assignment_done_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore',
            name='done_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
