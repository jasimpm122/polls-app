# Generated by Django 3.2.12 on 2024-01-14 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.choice'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]