# Generated by Django 3.2.15 on 2022-10-08 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=25)),
                ('house_name', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('pin_code', models.IntegerField(db_column='pin code')),
                ('email', models.CharField(max_length=25)),
                ('phone_no', models.CharField(db_column='phone no', max_length=20)),
                ('login_id', models.IntegerField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
