# Generated by Django 3.2.6 on 2021-08-20 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_alter_song_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='fecha',
            field=models.DateTimeField(null=True),
        ),
    ]
