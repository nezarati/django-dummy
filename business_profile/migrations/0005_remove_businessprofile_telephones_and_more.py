# Generated by Django 5.0.2 on 2024-02-27 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_profile', '0004_rename_familyname_fullname_family_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessprofile',
            name='telephones',
        ),
        migrations.RemoveField(
            model_name='businessprofile',
            name='web_links',
        ),
        migrations.RemoveField(
            model_name='businessprofile',
            name='work_week',
        ),
        migrations.AddField(
            model_name='namedtelephone',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='business_profile.businessprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weblink',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='business_profile.businessprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workday',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='business_profile.businessprofile'),
            preserve_default=False,
        ),
    ]
