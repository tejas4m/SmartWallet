# Generated by Django 3.2.5 on 2021-07-15 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userincome', '0003_alter_source_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]