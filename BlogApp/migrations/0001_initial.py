# Generated by Django 4.1.3 on 2022-11-25 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=200)),
                ('avatar', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogApp.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogApp.category')),
            ],
        ),
    ]
