# Generated by Django 2.1.4 on 2018-12-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date')),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_Name', models.CharField(max_length=200)),
                ('Task_Discription', models.CharField(max_length=200)),
                ('Complete_date', models.DateTimeField(verbose_name='complete date')),
            ],
        ),
    ]