# Generated by Django 4.1.4 on 2023-01-19 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fucus', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('kcalorie', models.IntegerField(default=0)),
                ('carbohydrate', models.IntegerField(default=0)),
                ('protein', models.IntegerField(default=0)),
                ('fat', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('food_number', models.IntegerField()),
                ('food_gram', models.IntegerField()),
                ('link', models.URLField()),
            ],
        ),
    ]
