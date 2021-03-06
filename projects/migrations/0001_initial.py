# Generated by Django 3.0.4 on 2020-09-16 04:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bugs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(blank='False', max_length=30)),
                ('heading', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('image', models.FileField(blank=True, upload_to='Bugs')),
                ('date', models.DateField(auto_now_add=True)),
                ('bug_status', models.CharField(choices=[('Unseen', 'Unseen'), ('Seen', 'Seen'), ('Processing', 'Processing'), ('Done', 'Done')], default='Unseen', max_length=30, verbose_name='Bug Status')),
                ('message', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Bugs',
                'verbose_name_plural': 'Bugs',
            },
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edit_attendance', models.BooleanField()),
                ('add_labour', models.BooleanField()),
                ('delete_labour', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Permissions',
                'verbose_name_plural': 'Permissions',
            },
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid_no', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('tender_number', models.CharField(max_length=500, verbose_name='Tender Number')),
                ('tender_name', models.CharField(max_length=500, verbose_name='Name of Work')),
                ('tender_description', models.TextField()),
                ('tender_submission_date', models.DateField(default=django.utils.timezone.now, verbose_name='Tender Submission Date')),
                ('tender_purchase_reciept', models.FileField(upload_to='', verbose_name='Tender Purchase Reciept')),
                ('tender_confirmation_reciept', models.FileField(upload_to='', verbose_name='Tender Confirmation Reciept')),
                ('physical_submission_date', models.DateField(default=django.utils.timezone.now, verbose_name='Physical Submission Date')),
                ('tech_bid_opening_date', models.DateField(default=django.utils.timezone.now, verbose_name='Technical Bid Opening Date')),
                ('bid_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, verbose_name='Bid Status')),
                ('bid_price_opening_date', models.DateField(blank=True, verbose_name='Bid price opening date')),
                ('prize_bid', models.CharField(max_length=50, verbose_name='Bid Price')),
            ],
            options={
                'verbose_name': 'Tender Lists',
                'verbose_name_plural': 'Tender Lists',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Start Date')),
                ('use_less', models.BooleanField(default=True)),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Tender')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Project',
            },
        ),
        migrations.CreateModel(
            name='other_contractors_bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractor_info', models.CharField(max_length=500, verbose_name='Other Contractors Information')),
                ('contractor_price', models.CharField(max_length=50, verbose_name='Bid')),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Tender')),
            ],
            options={
                'verbose_name': 'Other Contractors',
                'verbose_name_plural': 'Other Contractors',
            },
        ),
    ]
