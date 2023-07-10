# Generated by Django 3.2.4 on 2021-11-24 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LearnIt', '0010_auto_20210907_1121'),
        ('Sales', '0031_alter_customercallreposnses_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityMainModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LearnIt.stage')),
            ],
            options={
                'unique_together': {('stage', 'name')},
            },
        ),
        migrations.CreateModel(
            name='ActivitySubModules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subModuleName', models.CharField(max_length=300, null=True)),
                ('ActivityMainModule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_module', to='Customer.activitymainmodule')),
            ],
            options={
                'verbose_name': 'Activity Sub modules',
            },
        ),
        migrations.CreateModel(
            name='BabyPics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('description', models.TextField(default='')),
                ('length', models.CharField(blank=True, max_length=50, null=True)),
                ('weigth', models.CharField(blank=True, max_length=50, null=True)),
                ('size', models.CharField(default=0, max_length=50)),
                ('image', models.ImageField(upload_to='BabyPics')),
            ],
            options={
                'verbose_name': 'Client Login Foetal Image',
            },
        ),
        migrations.CreateModel(
            name='CustomSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(default='empty custom symptom', max_length=200)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DailyTrackerModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'daily tracker module',
                'verbose_name_plural': 'daily tracker modules',
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Meal (Manual)',
            },
        ),
        migrations.CreateModel(
            name='MedicineTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Medicine time(manual)',
            },
        ),
        migrations.CreateModel(
            name='PainScale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Pain Scale (manual)',
            },
        ),
        migrations.CreateModel(
            name='SymptomsCategory',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Customer.symptomscategory')),
            ],
        ),
        migrations.CreateModel(
            name='PositiveSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('positive', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('symptom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positive_symptom', to='Customer.symptoms')),
            ],
        ),
        migrations.CreateModel(
            name='PositiveCustomSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('positive', models.BooleanField(default=False)),
                ('symptoms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positive_custom_symptom', to='Customer.customsymptoms')),
            ],
        ),
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=300, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Medicines', to='Customer.medicinetime')),
            ],
            options={
                'unique_together': {('customer', 'time', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('appointmentDate', models.DateField(blank=True, null=True)),
                ('scantDate', models.DateField(blank=True, null=True)),
                ('ultraSound', models.FileField(null=True, upload_to='ultrasound')),
                ('bloodReport', models.FileField(null=True, upload_to='bloodreport')),
                ('antenatalChart', models.FileField(null=True, upload_to='antenatal')),
                ('bp', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LastUpdateDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet', models.DateTimeField(default=django.utils.timezone.now)),
                ('medicine', models.DateTimeField(default=django.utils.timezone.now)),
                ('activity', models.DateTimeField(default=django.utils.timezone.now)),
                ('symptom', models.DateTimeField(default=django.utils.timezone.now)),
                ('exercise', models.DateTimeField(default=django.utils.timezone.now)),
                ('contraction', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_update', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearnIt.stage')),
            ],
        ),
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearnIt.stage')),
            ],
            options={
                'unique_together': {('stage', 'name')},
            },
        ),
        migrations.CreateModel(
            name='ExerciseConsent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('consent', models.BooleanField(default=False)),
                ('criticalityChange', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Sales.criticalitychange')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomExercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('customer', 'name')},
            },
        ),
        migrations.CreateModel(
            name='CustomActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('time', models.TimeField()),
                ('contraction', models.IntegerField(blank=True, null=True)),
                ('interval', models.DurationField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('painScale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Customer.painscale')),
            ],
        ),
        migrations.CreateModel(
            name='CompletedExercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_exercise', to='Customer.exercises')),
            ],
        ),
        migrations.CreateModel(
            name='CompletedCustomActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completedCustom', to='Customer.customactivity')),
            ],
        ),
        migrations.CreateModel(
            name='CaloriesBurnt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=5, default=0, max_digits=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TakenMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('taken', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('medicine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MedicineDetail', to='Customer.medicines')),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('medicine', 'customer', 'date')},
            },
        ),
        migrations.CreateModel(
            name='SymptomsInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('others', models.CharField(blank=True, max_length=500, null=True)),
                ('bloodSugar', models.CharField(blank=True, max_length=500, null=True)),
                ('bloodPressure', models.CharField(blank=True, max_length=500, null=True)),
                ('report', models.CharField(blank=True, max_length=500, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('customer', 'date')},
            },
        ),
        migrations.CreateModel(
            name='DietTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('food', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('meal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Customer.meal')),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('customer', 'date', 'meal')},
            },
        ),
        migrations.CreateModel(
            name='CompletedCustomeExercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_custom_exercise', to='Customer.customexercises')),
            ],
            options={
                'unique_together': {('exercise', 'date')},
            },
        ),
        migrations.CreateModel(
            name='CompletedActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('daily_tracker_submodules', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Completed_activity', to='Customer.activitysubmodules')),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('customer', 'date', 'daily_tracker_submodules')},
            },
        ),
    ]
