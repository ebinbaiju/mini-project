# Generated by Django 5.0.1 on 2024-02-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phonenumber', models.IntegerField()),
                ('username', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('conformpassword', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
