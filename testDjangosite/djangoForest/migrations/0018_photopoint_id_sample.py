# Generated by Django 4.1.3 on 2023-02-19 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoForest', '0017_remove_profile_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photopoint',
            name='id_sample',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoForest.sample', verbose_name='Проба'),
        ),
    ]