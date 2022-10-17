# Generated by Django 3.2.15 on 2022-10-08 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('o_id', models.IntegerField()),
                ('date', models.DateField()),
                ('mode_of_payment', models.CharField(max_length=25)),
                ('amount', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
    ]
