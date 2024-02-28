# Generated by Django 5.0.2 on 2024-02-27 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FullName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.TextField()),
                ('givenName', models.TextField()),
                ('middleName', models.TextField()),
                ('familyName', models.TextField()),
                ('suffix', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NamedTelephone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PostalAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.TextField()),
                ('region', models.TextField()),
                ('city', models.TextField()),
                ('addressLine', models.TextField()),
                ('postalCode', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WebLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('value', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(6, 'شنبه'), (0, 'یک\u200cشنبه'), (1, 'دوشنبه'), (2, 'سه\u200cشنبه'), (3, 'چهارشنبه'), (4, 'پنج\u200cشنبه'), (5, 'جمعه')])),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('limit', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='business_profile.basemodel')),
                ('gender', models.IntegerField(choices=[(1, 'ندارد'), (2, 'مرد'), (3, 'زن')])),
                ('place_name', models.TextField()),
                ('tagline', models.TextField()),
                ('description', models.TextField()),
                ('note', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('expires_at', models.DateField()),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business_profile.city')),
                ('fellowship', models.ManyToManyField(related_name='fellowship_skills', to='business_profile.skill')),
                ('geoAddress', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business_profile.postaladdress')),
                ('insurances', models.ManyToManyField(to='business_profile.insurance')),
                ('localities', models.ManyToManyField(to='business_profile.locality')),
                ('person_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business_profile.fullname')),
                ('services', models.ManyToManyField(related_name='service_skills', to='business_profile.skill')),
                ('specialty', models.ManyToManyField(related_name='specialty_skills', to='business_profile.skill')),
                ('subspecialty', models.ManyToManyField(related_name='subspecialty_skills', to='business_profile.skill')),
                ('telephones', models.ManyToManyField(to='business_profile.namedtelephone')),
                ('types', models.ManyToManyField(related_name='type_skills', to='business_profile.skill')),
                ('web_links', models.ManyToManyField(to='business_profile.weblink')),
                ('work_week', models.ManyToManyField(to='business_profile.workday')),
            ],
            bases=('business_profile.basemodel',),
        ),
    ]