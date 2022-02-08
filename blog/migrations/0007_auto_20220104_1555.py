# Generated by Django 3.2.6 on 2022-01-04 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20211229_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(default='New', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='watch',
            name='date_creation',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='watch',
            name='condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.condition'),
        ),
    ]