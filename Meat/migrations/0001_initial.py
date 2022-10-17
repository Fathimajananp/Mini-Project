# Generated by Django 3.2.15 on 2022-10-08 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.IntegerField(blank=True, null=True)),
                ('meat_name', models.CharField(max_length=30)),
                ('items', models.CharField(max_length=25)),
                ('type', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=50)),
                ('price_kg', models.CharField(db_column='price/kg', max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'meats',
                'managed': False,
            },
        ),
    ]