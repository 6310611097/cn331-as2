# Generated by Django 4.1.1 on 2022-09-24 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('Id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=64)),
                ('Credit', models.CharField(max_length=1)),
                ('Term', models.CharField(default='1', max_length=1)),
                ('Year', models.CharField(default='2022', max_length=4)),
                ('remainSeat', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ManyToManyField(to='log_in.subject')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log_in.subject')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log_in.student')),
            ],
        ),
    ]
