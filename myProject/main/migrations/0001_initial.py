# Generated by Django 4.0.2 on 2022-03-02 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=40)),
                ('d_img_url', models.CharField(default='https://media.istockphoto.com/photos/mallard-duck-on-white-background-picture-id464988959', max_length=150)),
            ],
        ),
    ]
