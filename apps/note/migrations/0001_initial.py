# Generated by Django 4.1.2 on 2022-10-30 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=60, null=True)),
                ('note', models.CharField(max_length=500)),
            ],
        ),
    ]
