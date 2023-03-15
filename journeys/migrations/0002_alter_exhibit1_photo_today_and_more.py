# Generated by Django 4.1.4 on 2023-02-08 12:32

from django.db import migrations, models
import django.db.models.deletion
import journeys.models


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit1',
            name='photo_today',
            field=models.ImageField(upload_to='photos', verbose_name='העלה תמונה שלך היום'),
        ),
        migrations.AlterField(
            model_name='exhibit1',
            name='photo_yaldut',
            field=models.ImageField(upload_to=journeys.models.user_directory_path, verbose_name='העלה תמונת ילדות'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='exhibit_1',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='journey', to='journeys.exhibit1'),
        ),
    ]
