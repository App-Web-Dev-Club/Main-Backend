# Generated by Django 5.0.1 on 2024-02-08 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_joined_date_remove_user_left_date'),
        ('inventory', '0002_alter_manager_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kh_project',
            name='project_lead',
        ),
        migrations.RemoveField(
            model_name='kh_club_members_attendanance',
            name='user',
        ),
        migrations.RemoveField(
            model_name='kh_project',
            name='kh_members',
        ),
        migrations.RemoveField(
            model_name='kh_club_members_attendanance',
            name='project',
        ),
        migrations.RemoveField(
            model_name='kids_permission',
            name='user',
        ),
        migrations.RemoveField(
            model_name='kids_punchtime',
            name='user',
        ),
        migrations.DeleteModel(
            name='KH_Club_Members',
        ),
        migrations.DeleteModel(
            name='KH_Club_Members_Attendanance',
        ),
        migrations.DeleteModel(
            name='KH_Project',
        ),
        migrations.DeleteModel(
            name='KIDS_Permission',
        ),
        migrations.DeleteModel(
            name='KIDS_PunchTime',
        ),
    ]
