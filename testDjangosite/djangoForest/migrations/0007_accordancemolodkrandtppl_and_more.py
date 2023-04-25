# Generated by Django 4.1.3 on 2022-12-18 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoForest', '0006_remove_quarter_id_forestly_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccordanceMolodKrAndTPPL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_accordance', models.CharField(max_length=300, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Соответ. молодняка кр. и тр. ПЛ',
                'verbose_name_plural': 'Соответ. молодняка кр. и тр. ПЛ',
            },
        ),
        migrations.CreateModel(
            name='AccordanceNoneAccordanceEconomy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_accordance_none_economy', models.CharField(max_length=300, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Соответ. не соответ. хозяйству',
                'verbose_name_plural': 'Соответ. не соответ. хозяйству ',
            },
        ),
        migrations.CreateModel(
            name='BonitetOrlov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_of_planting', models.FloatField(verbose_name='Возраст насаждения')),
                ('height_planting_for_bonitet_class', models.CharField(max_length=300, verbose_name='Высота насаждения по классам бонитета, м')),
                ('class_bonitet', models.CharField(max_length=300, verbose_name='Класс бонитета')),
            ],
            options={
                'verbose_name': 'Бонитет по Орлову',
                'verbose_name_plural': 'Бонитет по Орлову',
            },
        ),
        migrations.CreateModel(
            name='CategoryGroundLFInNoneAccordance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_category_ground', models.CharField(max_length=300, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Кат. земель лф в случ. несоотв.',
                'verbose_name_plural': 'Кат. земель лф в случ. несоотв.',
            },
        ),
        migrations.CreateModel(
            name='CategoryOfForestFundLands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=350, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Категория земель лесного фонда',
                'verbose_name_plural': 'Категория земель лесного фонда',
            },
        ),
        migrations.CreateModel(
            name='Economy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_economy', models.CharField(max_length=300, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Хозяйство',
                'verbose_name_plural': 'Хозяйство',
            },
        ),
        migrations.CreateModel(
            name='ForestAreas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_forest_areas', models.CharField(max_length=300, verbose_name='Наименование')),
                ('composition_of_forest_areas', models.CharField(max_length=500, verbose_name='Состав лесных районов')),
                ('comm', models.CharField(max_length=500, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Лесные районы',
                'verbose_name_plural': 'Лесные районы',
            },
        ),
        migrations.CreateModel(
            name='ForestProtectionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_forest_protection_category', models.CharField(max_length=350, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Категория защитности лесов',
                'verbose_name_plural': 'Категория защитности лесов',
            },
        ),
        migrations.CreateModel(
            name='MethodOfReforestation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_method', models.CharField(max_length=350, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Способ лесовосстановления',
                'verbose_name_plural': 'Способ лесовосстановления',
            },
        ),
        migrations.CreateModel(
            name='PurposeOfForests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_purpose', models.CharField(max_length=350, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Целевое назначение лесов',
                'verbose_name_plural': 'Целевое назначение лесов',
            },
        ),
        migrations.CreateModel(
            name='TypeForestGrowingConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtypes_of_humidity', models.CharField(max_length=300, verbose_name='Подтипы влажности')),
                ('subtypes_of_rich', models.CharField(max_length=300, verbose_name='Подтипы богатства')),
                ('type_forest_growing_conditions', models.CharField(max_length=300, verbose_name='Тип лесорастительный условий')),
            ],
            options={
                'verbose_name': 'Тип лесорастительный условий',
                'verbose_name_plural': 'Тип лесорастительный условий',
            },
        ),
        migrations.AddField(
            model_name='sample',
            name='id_quarter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoForest.quarter',
                                    verbose_name='Квартал'),
        ),
        migrations.AddField(
            model_name='sample',
            name='soil_lot',
            field=models.CharField(max_length=300, null=True, verbose_name='Выдел'),
        ),
        migrations.AlterField(
            model_name='list',
            name='id_sample',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoForest.sample',
                                    verbose_name='Проба'),
        ),
        migrations.AlterField(
            model_name='listregion',
            name='sample_region',
            field=models.CharField(max_length=300, verbose_name='Плошадь участка, га'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sample_area',
            field=models.FloatField(verbose_name='Площадь пробы, га'),
        ),
    ]