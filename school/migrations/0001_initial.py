# Generated by Django 2.2.6 on 2019-11-28 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('code', models.CharField(max_length=25, unique=True)),
                ('career_type', models.CharField(choices=[('STARTER', 'STARTER'), ('BASIC', 'BASIC'), ('INTERMEDIATE', 'INTERMEDIATE'), ('ADVANCED', 'ADVANCED')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='account.Profile')),
                ('code', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('code', models.CharField(auto_created=True, max_length=25)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='account.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(auto_created=True, max_length=25, unique=True)),
                ('name', models.CharField(max_length=80, unique=True)),
                ('career', models.ManyToManyField(blank=True, to='school.Career')),
                ('professors', models.ManyToManyField(blank=True, to='school.Professor')),
                ('students', models.ManyToManyField(blank=True, to='school.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True, help_text='mm/dd/yy')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('grade', models.CharField(choices=[('01', '1'), ('02', '2'), ('03', '3'), ('04', '4'), ('05', '5'), ('06', '6'), ('07', '7'), ('08', '8'), ('09', '9'), ('10', '10')], max_length=2)),
                ('grade_creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.Profile')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Absences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True, help_text='mm/dd/yy')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('absence', models.CharField(choices=[('.5', '0.5'), ('01', '1')], max_length=2)),
                ('absence_creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.Profile')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.Student')),
            ],
        ),
    ]