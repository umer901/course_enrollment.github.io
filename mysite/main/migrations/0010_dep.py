# Generated by Django 4.1.3 on 2022-12-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_section_id_user_course_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('section_ID', models.IntegerField()),
                ('instructor_name', models.CharField(max_length=150)),
            ],
        ),
    ]