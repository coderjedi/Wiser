# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-02-03 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newres', '0006_auto_20190129_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=5000000)),
            ],
        ),
        migrations.DeleteModel(
            name='Logindata',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='year_of_study',
            new_name='education_level',
        ),
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='selectedchoice',
        ),
        migrations.RemoveField(
            model_name='question',
            name='user_id',
        ),
        migrations.AddField(
            model_name='question',
            name='question_format',
            field=models.CharField(choices=[('mcq', 'PRE ASSESSMENT'), ('openended', 'OPENENDED')], max_length=450, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('preassessment', 'PRE ASSESSMENT'), ('postassessment', 'PRE ASSESSMENT'), ('experiment', 'EXPERIMENT'), ('placebo', 'PLACEBO')], max_length=450, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='category',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdata',
            name='emailid',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdata',
            name='gender',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdata',
            name='password',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdata',
            name='status',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='choice1',
            field=models.CharField(max_length=4500, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice2',
            field=models.CharField(max_length=4500, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice3',
            field=models.CharField(max_length=4500, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice4',
            field=models.CharField(max_length=4500, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=45000),
        ),
        migrations.AddField(
            model_name='answer',
            name='question_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newres.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newres.Userdata'),
        ),
    ]
