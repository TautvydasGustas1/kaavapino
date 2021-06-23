# Generated by Django 2.2.13 on 2021-06-16 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0112_documenttemplate_image_template'),
    ]

    def create_common_phases(apps, schema_editor):
        CommonProjectPhase = apps.get_model('projects', 'CommonProjectPhase')
        ProjectPhase = apps.get_model('projects', 'ProjectPhase')

        for phase in ProjectPhase.objects.all():
            common_phase, _ = CommonProjectPhase.objects.get_or_create(
                name=phase.name,
                defaults={
                    "color": phase.color,
                    "color_code": phase.color_code,
                    "list_prefix": phase.list_prefix
                },
            )

            if phase.index > common_phase.index:
                common_phase.index = phase.index
                common_phase.save()

            phase.common_project_phase = common_phase
            phase.save()

    operations = [
        migrations.CreateModel(
            name='CommonProjectPhase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('color', models.CharField(blank=True, max_length=64, verbose_name='color')),
                ('color_code', models.CharField(blank=True, max_length=10, verbose_name='color code')),
                ('list_prefix', models.CharField(blank=True, max_length=2, null=True, verbose_name='list prefix')),
                ('index', models.PositiveIntegerField(default=0, verbose_name='index')),
            ],
            options={
                'verbose_name': 'common project phase',
                'verbose_name_plural': 'common project phases',
                'ordering': ('index',),
            },
        ),
        migrations.AddField(
            model_name='projectphase',
            name='common_project_phase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='phases', to='projects.CommonProjectPhase', verbose_name='common project phase'),
        ),
        migrations.RunPython(create_common_phases, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='projectphase',
            name='color',
        ),
        migrations.RemoveField(
            model_name='projectphase',
            name='color_code',
        ),
        migrations.RemoveField(
            model_name='projectphase',
            name='list_prefix',
        ),
        migrations.RemoveField(
            model_name='projectphase',
            name='name',
        ),
        migrations.AlterField(
            model_name='projectphase',
            name='common_project_phase',
            field=models.ForeignKey(null=False, on_delete=django.db.models.deletion.PROTECT, related_name='phases', to='projects.CommonProjectPhase', verbose_name='common project phase'),
        )
    ]