# Generated by Django 4.2.2 on 2023-07-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='XLModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exel_field', models.FileField(upload_to='xlfiles/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
