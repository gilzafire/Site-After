# Generated by Django 5.1 on 2024-09-13 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ritz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat', models.CharField(max_length=50)),
                ('temps_de_preparation', models.CharField(max_length=50)),
                ('cout', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['pseudo'],
            },
        ),
        migrations.CreateModel(
            name='After',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.DateTimeField()),
                ('ritz', models.ManyToManyField(to='shared.ritz')),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur_After',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('est_DJ', models.BooleanField()),
                ('fk_After', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.after')),
                ('fk_utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.utilisateur')),
            ],
        ),
        migrations.AddField(
            model_name='after',
            name='participants',
            field=models.ManyToManyField(through='shared.Utilisateur_After', to='shared.utilisateur'),
        ),
    ]
