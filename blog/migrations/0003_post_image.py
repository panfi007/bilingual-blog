# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=blog.models.get_image_filename, verbose_name=b'Image', blank=True),
        ),
    ]
