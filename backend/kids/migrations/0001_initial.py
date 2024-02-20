# Generated by Django 5.0.2 on 2024-02-20 13:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('shot_description', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('conducting_organization', models.CharField(max_length=255)),
                ('registation_date', models.DateTimeField()),
                ('website_link', models.URLField()),
                ('registation_link', models.URLField()),
                ('whatsapplink', models.URLField()),
                ('gcr_code', models.CharField(max_length=255)),
                ('end_Date', models.DateTimeField()),
                ('banner', models.ImageField(upload_to='hacakthon/banner/')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KH_Club_Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.CharField(choices=[('3D', '3d'), ('AI', 'Ai'), ('WEB AND APP', 'Web_And_App'), ('IOT AND ROBOTICS', 'Iot_And_Robotics'), ('XOR', 'Xor'), ('CYBER SECURITY', 'Cyber security'), ('COMPETITIVE PROGRAMMING', 'Competitive Programming'), ('BUILD CLUB', 'Build club'), ('GDSC', 'Google Developers Student Club'), ('Neural network', 'Neural network '), ('KH Core', 'Khacks Core Team'), ('Ecell core', 'Ecell Core'), ('Accelerator club', 'Accelerator club'), ('Women Entrepreneur Club', 'Women Entrepreneur Club'), ('Resource hub', 'resource hub'), ('Start up', 'start up'), ('Kreatives core', 'kreatives core'), ('TEDX', 'TEDX'), ('Design club', 'Design club'), ('Writters club', 'Writters club'), ('KIDS', 'KIDS')], max_length=100)),
                ('permission', models.CharField(choices=[('ADMIN', 'Admin'), ('CLUB_LEADER', 'ClubLeader'), ('MEMBER', 'Member')], max_length=100)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('left_date', models.DateField(blank=True, null=True)),
                ('regno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='club_member', to='api.student')),
            ],
        ),
        migrations.CreateModel(
            name='KH_Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('accepted', 'Accepted'), ('rejected', 'Rejected'), ('onprocess', 'On Process'), ('completed', 'Completed'), ('hold', 'Hold')], max_length=255)),
                ('kh_members', models.ManyToManyField(to='kids.kh_club_members')),
                ('project_lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_led', to='kids.kh_club_members')),
            ],
        ),
        migrations.CreateModel(
            name='KH_Club_Members_Attendanance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('work_done', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_attendances', to='kids.kh_club_members')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kids.kh_project')),
            ],
        ),
        migrations.CreateModel(
            name='KIDS_Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('type', models.CharField(choices=[('late_night', 'Late_Night'), ('1st_year', '1st_Year'), ('holiday ', 'Holiday ')], max_length=100)),
                ('user', models.ManyToManyField(to='api.student')),
            ],
        ),
        migrations.CreateModel(
            name='KIDS_PunchTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('regno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
