# Generated by Django 5.1.3 on 2025-01-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(default="Ma'lumot qo'shilmadi.", verbose_name='Tavsifi'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='Elektron pochta manzili'),
        ),
    ]