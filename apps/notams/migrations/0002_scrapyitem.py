# Generated by Django 2.1 on 2018-08-09 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=100, null=True)),
                ('data', models.TextField()),
            ],
        ),
    ]