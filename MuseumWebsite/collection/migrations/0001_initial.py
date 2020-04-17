# Generated by Django 3.0.4 on 2020-03-13 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artefact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('title', models.CharField(max_length=100, verbose_name='Title of artefact')),
                ('description', models.TextField()),
                ('artist', models.CharField(max_length=100)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-publish_date',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('artefact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='collection.Artefact')),
            ],
        ),
    ]
