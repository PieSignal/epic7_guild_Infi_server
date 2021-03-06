# Generated by Django 3.0.2 on 2020-03-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill', models.CharField(max_length=30)),
                ('target', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='buff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='debuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DefensePreset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Defense', models.IntegerField()),
                ('HP', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Heros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SearchKey', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('rarity', models.IntegerField()),
                ('classType', models.CharField(max_length=20)),
                ('element', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='notic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=200, null=True)),
                ('contents', models.TextField(max_length=4000, null=True)),
                ('important', models.BooleanField(default=False)),
                ('linkName', models.CharField(blank=True, max_length=20, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='epic/image')),
            ],
        ),
        migrations.CreateModel(
            name='tips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=200, null=True)),
                ('memo', models.TextField(blank=True, max_length=500, null=True)),
                ('important', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='epic/image')),
                ('imageLink', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('UPW', models.CharField(max_length=100)),
                ('Signed', models.BooleanField(default=False)),
                ('isManager', models.BooleanField(default=False)),
            ],
        ),
    ]
