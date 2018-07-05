# Generated by Django 2.0.6 on 2018-07-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jackpot', '0006_remove_hexabet_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Singlebet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(verbose_name='Date Published')),
                ('country', models.CharField(max_length=200)),
                ('home_team', models.CharField(max_length=200)),
                ('home_score', models.IntegerField(default=0)),
                ('away_score', models.IntegerField(default=0)),
                ('away_team', models.CharField(max_length=200)),
                ('safety', models.CharField(default='', max_length=200)),
                ('prediction', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Won', 'Won'), ('Lost', 'Lost')], max_length=100)),
            ],
        ),
    ]