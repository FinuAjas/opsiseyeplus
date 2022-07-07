# Generated by Django 3.2.3 on 2022-07-06 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='specs/')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]