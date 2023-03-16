# Generated by Django 4.1.6 on 2023-03-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=10)),
                ('meal_kcalorie', models.IntegerField(null=True)),
                ('meal_protien', models.IntegerField(null=True)),
                ('meal_fat', models.IntegerField(null=True)),
                ('meal_carbohydrate', models.IntegerField(null=True)),
                ('need_kcalorie', models.IntegerField(null=True)),
                ('need_protien', models.IntegerField(null=True)),
                ('need_fat', models.IntegerField(null=True)),
                ('need_carbohydrate', models.IntegerField(null=True)),
                ('foods', models.ManyToManyField(null=True, to='foods.food')),
            ],
        ),
    ]
