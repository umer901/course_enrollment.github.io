# Generated by Django 4.1.3 on 2022-12-08 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_course_id_user_section_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='section_ID',
            new_name='course_ID',
        ),
    ]
