# Generated by Django 3.1.7 on 2021-05-20 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0005_auto_20210502_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m10form',
            name='amount',
            field=models.IntegerField(blank=True, null=True, verbose_name='مبلغ'),
        ),
        migrations.AlterField(
            model_name='m10form',
            name='applicator',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='درخواست کننده'),
        ),
        migrations.AlterField(
            model_name='m10form',
            name='descript',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='موافقه تادیه'),
        ),
        migrations.AlterField(
            model_name='m10form',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='ضرورت پیشکی'),
        ),
        migrations.AlterField(
            model_name='m10form',
            name='issue_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ منظوری'),
        ),
        migrations.AlterField(
            model_name='m10form',
            name='item_type',
            field=models.CharField(blank=True, choices=[('SA', 'معاش'), ('PA', 'مسافرت'), ('PU', 'خریداری')], max_length=2, null=True, verbose_name='نوع پیشکی'),
        ),
        migrations.AlterField(
            model_name='m10form',
            name='suggestion_num',
            field=models.IntegerField(blank=True, null=True, verbose_name='نمبر درخواستی'),
        ),
        migrations.AlterField(
            model_name='m11form',
            name='document_num',
            field=models.IntegerField(blank=True, null=True, verbose_name='شماره مکتبوب'),
        ),
        migrations.AlterField(
            model_name='m11form',
            name='issued_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ صدور'),
        ),
        migrations.AlterField(
            model_name='m11formdetail',
            name='dedicated',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='تهیه شده'),
        ),
        migrations.AlterField(
            model_name='m11formdetail',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='تشریحات'),
        ),
        migrations.AlterField(
            model_name='m11formdetail',
            name='expenses',
            field=models.IntegerField(blank=True, null=True, verbose_name='مصارف'),
        ),
        migrations.AlterField(
            model_name='m11formdetail',
            name='form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='input.m11form'),
        ),
        migrations.AlterField(
            model_name='m3form',
            name='issued_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ صدور'),
        ),
        migrations.AlterField(
            model_name='m3form',
            name='purchase_order_num',
            field=models.IntegerField(blank=True, null=True, verbose_name='نمبر امر خریداری'),
        ),
        migrations.AlterField(
            model_name='m3form',
            name='purchase_suggestion_num',
            field=models.IntegerField(blank=True, null=True, verbose_name='نمبر درخواست خریداری'),
        ),
        migrations.AlterField(
            model_name='m3form',
            name='suggestion_form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='input.suggestionform', verbose_name='شماره فورم پیشنهاد'),
        ),
        migrations.AlterField(
            model_name='m3formdetail',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='تشریحات'),
        ),
        migrations.AlterField(
            model_name='m3formdetail',
            name='item',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='جنس'),
        ),
        migrations.AlterField(
            model_name='m3formdetail',
            name='module',
            field=models.CharField(blank=True, choices=[('P', 'قطی'), ('C', 'کارتن'), ('N', 'عدد')], max_length=1, null=True, verbose_name='فیات'),
        ),
        migrations.AlterField(
            model_name='m3formdetail',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='مجموع قیمت'),
        ),
        migrations.AlterField(
            model_name='m3formdetail',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='تعداد/دانه'),
        ),
        migrations.AlterField(
            model_name='m7form',
            name='issued_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='m7form',
            name='purchase_place',
            field=models.CharField(blank=True, default='بازار هرات', max_length=20, null=True, verbose_name='اخذ گردیده از'),
        ),
        migrations.AlterField(
            model_name='m7form',
            name='report_num',
            field=models.IntegerField(blank=True, null=True, verbose_name='نمبر راپور'),
        ),
        migrations.AlterField(
            model_name='m7form',
            name='suggestion_form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='input.suggestionform', verbose_name='نمبر فرمایش'),
        ),
        migrations.AlterField(
            model_name='m7formdetail',
            name='amount',
            field=models.IntegerField(blank=True, null=True, verbose_name='مبلغ'),
        ),
        migrations.AlterField(
            model_name='m7formdetail',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='تشریحات'),
        ),
        migrations.AlterField(
            model_name='m7formdetail',
            name='fiyat',
            field=models.IntegerField(blank=True, null=True, verbose_name='فیات'),
        ),
        migrations.AlterField(
            model_name='m7formdetail',
            name='module',
            field=models.CharField(blank=True, choices=[('P', 'قطی'), ('C', 'کارتن'), ('N', 'عدد')], max_length=1, null=True, verbose_name='واحد'),
        ),
        migrations.AlterField(
            model_name='m7formdetail',
            name='observations',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='ملاحظات'),
        ),
        migrations.AlterField(
            model_name='m7formdetail',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='مقدار'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='addminstartion_commandment',
            field=models.TextField(blank=True, null=True, verbose_name='حکم بخش اداری'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='addminstration_final',
            field=models.TextField(blank=True, null=True, verbose_name='اجرات بخش اداری'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='advice_commitee',
            field=models.TextField(blank=True, null=True, verbose_name='نظر هیت'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='dean',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='اسم ریس'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='dean_commandment',
            field=models.TextField(blank=True, null=True, verbose_name='حکم ریس'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='deanship',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='مقام مربوطه'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ریاست مربوطه'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضحات'),
        ),
        migrations.AlterField(
            model_name='suggestionform',
            name='topic',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='موضوغ'),
        ),
    ]