# Generated by Django 4.1.3 on 2024-09-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TGID', models.CharField(max_length=100, unique=True)),
                ('username', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('highest_education', models.CharField(max_length=100)),
                ('is_employed', models.BooleanField()),
                ('needs', models.TextField()),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_pic', models.URLField(blank=True, null=True)),
                ('is_joined_group', models.BooleanField(default=False)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
