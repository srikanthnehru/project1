# Generated by Django 3.0.7 on 2020-06-09 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guruname', models.CharField(max_length=40)),
                ('gurucode', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='coursecode',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='guru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Guru', to='shop.Guru'),
        ),
    ]