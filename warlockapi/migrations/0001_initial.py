# Generated by Django 4.1.5 on 2023-02-04 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stamina', models.CharField(max_length=20)),
                ('notes', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CastType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=300)),
                ('traits', models.CharField(max_length=300)),
                ('notes', models.CharField(max_length=300)),
                ('spells', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Npc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stamina', models.CharField(max_length=20)),
                ('notes', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='NpcType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('bio', models.CharField(max_length=100)),
                ('profile_image_url', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=25)),
                ('created_on', models.DateField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NpcCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npctype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warlockapi.npctype')),
            ],
        ),
        migrations.CreateModel(
            name='NpcCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warlockapi.campaign')),
                ('npc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warlockapi.npc')),
            ],
        ),
        migrations.AddField(
            model_name='npc',
            name='npccategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warlockapi.npccategory'),
        ),
        migrations.AddField(
            model_name='npc',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warlockapi.user'),
        ),
        migrations.CreateModel(
            name='CharacterCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warlockapi.campaign')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warlockapi.character')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='warlockapi.user'),
        ),
        migrations.CreateModel(
            name='CastCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warlockapi.casttype')),
            ],
        ),
        migrations.CreateModel(
            name='CastCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warlockapi.campaign')),
                ('cast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warlockapi.cast')),
            ],
        ),
        migrations.AddField(
            model_name='cast',
            name='castcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warlockapi.castcategory'),
        ),
        migrations.AddField(
            model_name='cast',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warlockapi.user'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='casts',
            field=models.ManyToManyField(through='warlockapi.CastCampaign', to='warlockapi.cast'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='npcs',
            field=models.ManyToManyField(through='warlockapi.NpcCampaign', to='warlockapi.npc'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warlockapi.user'),
        ),
    ]
