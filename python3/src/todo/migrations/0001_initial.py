# Generated by Django 2.2.5 on 2019-11-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('todo_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='TODOタイトル')),
                ('detail', models.CharField(max_length=300, verbose_name='TODO詳細')),
                ('insert_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
            ],
        ),
    ]
