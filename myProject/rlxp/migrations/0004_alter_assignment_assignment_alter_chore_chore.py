# Generated by Django 4.0.2 on 2022-04-24 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rlxp', '0003_alter_chore_chore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assignment',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chore',
            name='chore',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]