# Generated by Django 3.0.5 on 2020-05-14 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gradebook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submit',
            name='assignment',
        ),
        migrations.AddField(
            model_name='submit',
            name='assignment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gradebook.Assignment'),
        ),
    ]
