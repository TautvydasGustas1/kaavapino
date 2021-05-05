# Generated by Django 2.2.13 on 2021-04-20 04:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0104_documentlinkfieldset_documentlinksection'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverviewFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('identifier', models.CharField(db_index=True, max_length=20, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w]+\\Z'), "Enter a valid 'identifier' consisting of Unicode letters, numbers or underscores.", 'invalid')], verbose_name='identifier')),
            ],
        ),
        migrations.CreateModel(
            name='OverviewFilterAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filters_by_subtype', models.BooleanField(default=False, verbose_name='filters project subtype overview')),
                ('filters_floor_area', models.BooleanField(default=False, verbose_name='filters project floor area overview')),
                ('filters_on_map', models.BooleanField(default=False, verbose_name='filters project map overview')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Attribute', verbose_name='attribute')),
                ('overview_filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='projects.OverviewFilter', verbose_name='overview filter')),
            ],
        ),
    ]