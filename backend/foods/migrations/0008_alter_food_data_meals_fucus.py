# Generated by Django 4.1.4 on 2023-01-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0007_alter_food_data_meals_fucus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_data',
            name='meals_fucus',
            field=models.CharField(choices=[("('1', '아침')", 'Breakfast'), ("('2', '점심')", 'Lunch'), ("('3', '저녁')", 'Dinner'), ("('0', '아침, 점심, 저녁')", 'All')], default="('1', '아침')", max_length=30),
        ),
    ]