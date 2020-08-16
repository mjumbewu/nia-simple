# Generated by Django 3.0.1 on 2020-01-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
                ('description', models.TextField()),
                ('goals', models.ManyToManyField(related_name='projects', to='nia.Goal', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='goal',
            name='values',
            field=models.ManyToManyField(related_name='goals', to='nia.Value', blank=True),
        ),
    ]
