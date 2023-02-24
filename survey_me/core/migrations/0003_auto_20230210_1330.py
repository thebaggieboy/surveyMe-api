# Generated by Django 3.0.6 on 2023-02-10 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230210_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='answersurvey',
            name='survey',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.CreateSurvey'),
        ),
        migrations.RemoveField(
            model_name='polls',
            name='answer_to',
        ),
        migrations.AddField(
            model_name='polls',
            name='answer_to',
            field=models.ManyToManyField(to='core.AnswerSurvey'),
        ),
    ]
