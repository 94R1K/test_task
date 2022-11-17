# Generated by Django 2.2.16 on 2022-09-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Product Name')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Product Description')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]