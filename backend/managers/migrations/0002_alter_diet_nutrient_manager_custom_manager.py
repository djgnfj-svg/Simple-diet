# Generated by Django 4.1.6 on 2023-03-15 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet_nutrient_manager',
            name='custom_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='managers.meal_food_type'),
        ),
    ]
