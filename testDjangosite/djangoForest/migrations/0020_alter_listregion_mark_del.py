# Generated by Django 4.1.3 on 2023-02-24 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoForest', '0019_alter_listregion_mark_del'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listregion',
            name='mark_del',
            field=models.BooleanField(null=True),
        ),
    ]
