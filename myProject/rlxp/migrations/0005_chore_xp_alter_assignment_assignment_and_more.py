# Generated by Django 4.0.2 on 2022-04-24 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rlxp', '0004_alter_assignment_assignment_alter_chore_chore'),
    ]

    operations = [
        migrations.AddField(
            model_name='chore',
            name='xp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='assignment',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='xp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='chore',
            name='chore',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='chore',
            name='recurring',
            field=models.BooleanField(default=True),
        ),
    ]
