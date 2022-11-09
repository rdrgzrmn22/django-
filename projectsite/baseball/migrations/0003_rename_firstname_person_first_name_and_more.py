# Generated by Django 4.1.3 on 2022-11-09 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0002_person'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='person',
            name='height',
            field=models.DecimalField(decimal_places=5, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='weight',
            field=models.DecimalField(decimal_places=5, max_digits=100, null=True),
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('dorm_latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('dorm_longtitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseball.person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
