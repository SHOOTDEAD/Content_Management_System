# Generated by Django 4.2.6 on 2023-12-07 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='files',
            field=models.ImageField(blank=True, upload_to='static/article/files/'),
        ),
    ]
