# Generated by Django 4.1.2 on 2022-10-16 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_branch', models.CharField(max_length=350, verbose_name='Наименование филиала')),
            ],
            options={
                'verbose_name': 'Филиал',
                'verbose_name_plural': 'Филиал',
            },
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_breed', models.CharField(max_length=350, verbose_name='Наименование породы')),
            ],
            options={
                'verbose_name': 'Порода',
                'verbose_name_plural': 'Порода',
            },
        ),
        migrations.CreateModel(
            name='DistrictForestly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_district_forestly', models.CharField(max_length=500, verbose_name='Наименование участкового лесничества')),
            ],
            options={
                'verbose_name': 'Участковое лесничество',
                'verbose_name_plural': 'Участковое лесничество',
            },
        ),
        migrations.CreateModel(
            name='Forestly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_forestly', models.CharField(max_length=500, verbose_name='Название лесничества')),
            ],
            options={
                'verbose_name': 'Лесничество',
                'verbose_name_plural': 'Лесничество',
            },
        ),
        migrations.CreateModel(
            name='ListRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('sample_region', models.CharField(max_length=300, verbose_name='Плошадь участка')),
                ('id_district_forestly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.districtforestly', verbose_name='Участковое лесничество')),
                ('id_forestly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.forestly', verbose_name='Лесничество')),
            ],
            options={
                'verbose_name': 'Перечетная ведомость участка',
                'verbose_name_plural': 'Перечетная ведомость участка',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=255, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Должности',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=255, verbose_name='ФИО')),
                ('phoneNumber', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail адресс')),
                ('id_branches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.branches', verbose_name='Филиал')),
                ('id_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.post', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Профили',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Reproduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_reproduction', models.CharField(max_length=500, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Вид воспроизводства',
                'verbose_name_plural': 'Вид воспроизводства',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_role', models.CharField(max_length=300, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Роли',
                'verbose_name_plural': 'Роли',
            },
        ),
        migrations.CreateModel(
            name='SubjectRF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_subject_RF', models.CharField(max_length=255, verbose_name='Наименования субъекта РФ')),
            ],
            options={
                'verbose_name': 'Субъект РФ',
                'verbose_name_plural': 'Субъект РФ',
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkingBreeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_breeds', models.CharField(max_length=255, verbose_name='Наименование рабочей породы')),
            ],
            options={
                'verbose_name': 'Рабочие породы',
                'verbose_name_plural': 'Рабочие породы',
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_area', models.IntegerField(verbose_name='Площадь пробы')),
                ('soil_lot', models.IntegerField(verbose_name='Выдел')),
                ('id_district_forestly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.districtforestly', verbose_name='Участковое лесничество')),
                ('id_forestly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.forestly', verbose_name='Лесничество')),
                ('id_list_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.listregion', verbose_name='Перечетная ведомость участка')),
                ('id_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.profile', verbose_name='Профиль')),
                ('id_subject_RF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.subjectrf', verbose_name='Субъект РФ')),
            ],
            options={
                'verbose_name': 'Проба',
                'verbose_name_plural': 'Проба',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter', models.IntegerField(verbose_name='Квартал')),
                ('soil_lot', models.IntegerField(verbose_name='Выдел')),
                ('sample_region', models.IntegerField(verbose_name='Площадь участка')),
                ('id_district_forestly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.districtforestly', verbose_name='Участковое лесничество')),
                ('id_forestly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.forestly', verbose_name='Лесничество')),
                ('id_subject_rf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.subjectrf', verbose_name='Субъект РФ')),
            ],
            options={
                'verbose_name': 'Участок',
                'verbose_name_plural': 'Участок',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='id_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.role', verbose_name='Роль'),
        ),
        migrations.AddField(
            model_name='profile',
            name='id_working_breeds',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.workingbreeds', verbose_name='Рабочая порода'),
        ),
        migrations.AddField(
            model_name='listregion',
            name='id_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.region', verbose_name='Участок'),
        ),
        migrations.AddField(
            model_name='listregion',
            name='id_subject_RF',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.subjectrf', verbose_name='Субъект РФ'),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to0_2', models.IntegerField(verbose_name='До 0,2')),
                ('from0_21To0_5', models.IntegerField(verbose_name='0,21 - 0,5')),
                ('from0_6To1_0', models.IntegerField(verbose_name='0,6 - 1,0')),
                ('from1_1to1_5', models.IntegerField(verbose_name='1,1 - 1,5')),
                ('from1_5', models.IntegerField(verbose_name='более 1,5')),
                ('max_height', models.IntegerField(verbose_name='Максимальная высота')),
                ('id_breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.breed', verbose_name='Порода')),
                ('id_sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.sample', verbose_name='Перечет')),
                ('id_type_of_reproduction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.reproduction', verbose_name='Вид воспроизводства')),
            ],
            options={
                'verbose_name': 'Перечет',
                'verbose_name_plural': 'Перечет',
            },
        ),
        migrations.CreateModel(
            name='GPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('flag_center', models.IntegerField(verbose_name='Флаг центра')),
                ('id_sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.sample', verbose_name='Проба')),
            ],
            options={
                'verbose_name': 'GPS',
                'verbose_name_plural': 'GPS',
            },
        ),
        migrations.AddField(
            model_name='branches',
            name='id_subject_RF',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoForest.subjectrf', verbose_name='Субъект РФ'),
        ),
    ]
