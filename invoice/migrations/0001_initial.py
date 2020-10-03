# Generated by Django 2.2.16 on 2020-10-01 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import invoice.validators


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
            name='Item',
            fields=[
                ('timestamps_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoice.TimeStamps')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            bases=('invoice.timestamps', models.Model),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('timestamps_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoice.TimeStamps')),
                ('invoice_number', models.CharField(max_length=255, unique=True)),
                ('vendor_name', models.CharField(max_length=40)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='', validators=[invoice.validators.validate_file_attachment])),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_created_by', to=settings.AUTH_USER_MODEL)),
                ('items', models.ManyToManyField(blank=True, null=True, to='invoice.Item')),
            ],
            bases=('invoice.timestamps', models.Model),
        ),
    ]
