# Generated by Django 4.0.6 on 2022-07-05 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('AL', 'Alive'), ('DD', 'Dead'), ('UN', 'Unknown')], default='UN', max_length=3)),
                ('desc', models.TextField()),
                ('gender', models.CharField(choices=[('ML', 'Male'), ('FL', 'Female'), ('GS', 'Genderless'), ('UN', 'Unknown')], default='UN', max_length=11)),
                ('race', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('universe', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('number_episode', models.IntegerField(verbose_name='номер серии')),
                ('desc', models.TextField(blank=True, null=True)),
                ('characters', models.ManyToManyField(blank=True, null=True, to='characters.character')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='birth_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='birth_location', to='characters.location'),
        ),
        migrations.AddField(
            model_name='character',
            name='current_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_location', to='characters.location'),
        ),
    ]
