# Generated by Django 4.1.4 on 2023-01-24 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='שם')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='שנה')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.school', verbose_name='בית ספר')),
            ],
        ),
        migrations.CreateModel(
            name='ClassGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.DecimalField(decimal_places=0, default=1, max_digits=2, verbose_name='מספר')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.grade', verbose_name='שכבה')),
                ('teacher', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.teacher', verbose_name='מורה')),
            ],
        ),
    ]
