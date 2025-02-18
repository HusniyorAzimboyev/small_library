# Generated by Django 5.1.2 on 2024-11-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_dummy'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='dummy',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
