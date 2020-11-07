# Generated by Django 3.1.2 on 2020-10-31 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=128)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('name', models.CharField(default='', max_length=48)),
                ('category', models.CharField(blank=True, max_length=24, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ending_point', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='itinerary_endp', to='w2gAPIdrf.step')),
                ('starting_point', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='itinerary_startp', to='w2gAPIdrf.step')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='itinerary_midp', to='w2gAPIdrf.step')),
            ],
            options={
                'verbose_name_plural': 'Itineraries',
            },
        ),
    ]
