# Generated by Django 3.2.7 on 2021-11-20 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('directionsInfo', models.TextField()),
                ('directionsURL', models.URLField()),
                ('image', models.URLField()),
                ('link_to_website', models.URLField()),
                ('marked', models.BooleanField()),
                ('visited', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitation_date', models.DateField(verbose_name='date visited')),
                ('content', models.TextField()),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parksApp.park')),
            ],
        ),
    ]