# Generated by Django 4.2.5 on 2023-11-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nutri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('Height', models.FloatField()),
                ('Weight', models.FloatField()),
                ('LifeStyle', models.CharField(choices=[('Extremely Inactive', 'Extremely Inactive'), ('Inactive', 'Inactive'), ('Moderately Active', 'Moderately Active'), ('Active', 'Active'), ('Extremely Active', 'Extremely Active')], max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Nutri',
            },
        ),
    ]
