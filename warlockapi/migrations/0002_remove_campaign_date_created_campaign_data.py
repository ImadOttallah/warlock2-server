# Generated by Django 4.1.5 on 2023-02-02 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warlockapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='date_created',
        ),
        migrations.AddField(
            model_name='campaign',
            name='data',
            field=models.DateTimeField(blank=True, default='2023-02-02 02:19:32', null=True),
        ),
    ]