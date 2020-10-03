# Generated by Django 2.2.16 on 2020-10-01 06:58

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
            name='TimeStamps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('timestamps_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.TimeStamps')),
                ('display_name', models.CharField(blank=True, max_length=250, null=True)),
                ('user_type', models.CharField(blank=True, choices=[('agent', 'Agent'), ('manager', 'Manager')], max_length=15, null=True)),
                ('profile_description', models.TextField(blank=True, max_length=999, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=255, null=True)),
                ('email_notification', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('accounts.timestamps', models.Model),
        ),
    ]