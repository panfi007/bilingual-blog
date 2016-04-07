# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_en',
            field=models.TextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='post',
            name='body_es',
            field=models.TextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_es',
            field=models.CharField(max_length=250, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=blog.models.get_image_filename, verbose_name='image', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='publish'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(default=b'draft', max_length=10, verbose_name='status', choices=[(b'draft', b'Draft'), (b'published', b'Published')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(null=True, verbose_name='date of birth', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.CharField(max_length=150, verbose_name='occupation'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(upload_to=b'users/%Y/%m/%d', verbose_name='photo', blank=True),
        ),
    ]
