# Generated by Django 3.1.7 on 2021-04-08 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pred_text', models.CharField(max_length=12)),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.description')),
            ],
        ),
    ]