# Generated by Django 3.2.7 on 2021-10-22 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting', '0002_initial'),
        ('students', '0002_student_user'),
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('movement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.movement')),
            ],
            options={
                'abstract': False,
            },
            bases=('accounting.positivemovement',),
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('movement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.movement')),
            ],
            options={
                'abstract': False,
            },
            bases=('accounting.negativemovement',),
        ),
        migrations.CreateModel(
            name='EngagementWallet',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.account')),
                ('current_level', models.PositiveSmallIntegerField(default=1, null=True)),
                ('student', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.student')),
            ],
            options={
                'abstract': False,
            },
            bases=('accounting.account',),
        ),
        migrations.AddField(
            model_name='coinwallet',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.student'),
        ),
    ]