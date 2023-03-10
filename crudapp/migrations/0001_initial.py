# Generated by Django 4.1.1 on 2023-02-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(blank=True, max_length=12, null=True)),
                ('clocation', models.CharField(blank=True, max_length=13, null=True)),
                ('cid', models.IntegerField(blank=True, null=True)),
                ('cstate', models.CharField(blank=True, max_length=14, null=True)),
                ('ccountry', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Principle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(blank=True, max_length=12, null=True)),
                ('pcity', models.CharField(blank=True, max_length=21, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('college', models.ManyToManyField(related_name='principle', to='crudapp.college')),
            ],
        ),
    ]
