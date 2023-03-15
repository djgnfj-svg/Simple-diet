# Generated by Django 4.1.6 on 2023-03-15 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metabolic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body_info_recode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('age', models.IntegerField()),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('gender', models.CharField(max_length=2)),
                ('general_activities', models.FloatField()),
                ('excise_activity', models.FloatField()),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metabolic.body_info')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
