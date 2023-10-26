# Generated by Django 4.2.6 on 2023-10-24 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_alter_laptop_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Хэштег',
                'verbose_name_plural': 'Хэштеги',
            },
        ),
        migrations.AddField(
            model_name='laptop',
            name='hashtags',
            field=models.ManyToManyField(to='categories.hashtag'),
        ),
    ]
