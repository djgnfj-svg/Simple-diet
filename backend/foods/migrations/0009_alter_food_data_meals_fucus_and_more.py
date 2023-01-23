# Generated by Django 4.1.4 on 2023-01-23 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0008_alter_food_data_meals_fucus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_data',
            name='meals_fucus',
            field=models.CharField(choices=[('breakfast', '아침'), ('lunch', '점심'), ('dinner', '저녁'), ('all', '아침, 점심, 저녁')], default='breakfast', max_length=30),
        ),
        migrations.AlterField(
            model_name='food_data',
            name='nutrient_fucus',
            field=models.CharField(choices=[('P', '단백질'), ('F', '지방'), ('C', '탄수화물')], default='P', max_length=2),
        ),
    ]
