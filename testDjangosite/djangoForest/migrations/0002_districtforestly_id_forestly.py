# Generated by Django 4.1.2 on 2022-11-07 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoForest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtforestly',
            name='id_forestly',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoForest.forestly', verbose_name='Лесничество'),
        ),
    ]