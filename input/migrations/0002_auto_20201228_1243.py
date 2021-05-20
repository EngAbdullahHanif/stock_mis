# Generated by Django 3.1.4 on 2020-12-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestionform',
            name='addminstartion_commandment',
            field=models.TextField(verbose_name='حکم بخش اداری'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='addminstration_final',
            field=models.TextField(verbose_name='اجرات بخش اداری'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='advice_commitee',
            field=models.TextField(verbose_name='نظر هیت'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='dean',
            field=models.CharField(max_length=30, verbose_name='اسم ریس'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='dean_commandment',
            field=models.TextField(verbose_name='حکم ریس'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='deanship',
            field=models.CharField(max_length=100, verbose_name='مقام مربوطه'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='department',
            field=models.CharField(max_length=100, verbose_name='ریاست مربوطه'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='description',
            field=models.TextField(verbose_name='توضحات'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='issued_date',
            field=models.DateField(verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='number',
            field=models.IntegerField(verbose_name='شماره'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='topic',
            field=models.CharField(max_length=100, verbose_name='موضوغ'),
        ),
    ]