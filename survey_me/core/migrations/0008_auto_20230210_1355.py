# Generated by Django 3.0.6 on 2023-02-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20230210_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='answer_1',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='answer_2',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='answer_3',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='answer_4',
        ),
        migrations.AddField(
            model_name='poll',
            name='choices',
            field=models.ManyToManyField(blank=True, related_name='related_polls', to='core.Choice'),
        ),
    ]