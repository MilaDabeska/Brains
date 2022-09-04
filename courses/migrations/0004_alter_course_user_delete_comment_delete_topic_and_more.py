# Generated by Django 4.1 on 2022-09-02 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_chapter_fileupload_textblock_ytlink_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='ytlink',
            name='yt_link_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.chapter'),
        ),
        migrations.AddField(
            model_name='textblock',
            name='text_block_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.chapter'),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='file_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.chapter'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]