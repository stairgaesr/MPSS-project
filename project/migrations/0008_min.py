# Generated by Django 2.2 on 2023-04-11 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_sale_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='min',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
            ],
        ),
    ]