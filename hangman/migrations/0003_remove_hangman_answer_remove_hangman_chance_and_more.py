# Generated by Django 4.0.5 on 2022-07-01 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0002_hangman_answer_hangman_chance_hangman_false_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hangman',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='hangman',
            name='chance',
        ),
        migrations.RemoveField(
            model_name='hangman',
            name='false',
        ),
        migrations.RemoveField(
            model_name='hangman',
            name='hidden',
        ),
        migrations.RemoveField(
            model_name='hangman',
            name='point',
        ),
    ]
