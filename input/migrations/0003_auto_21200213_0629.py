# Generated by Django 3.1.7 on 2120-02-13 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0002_auto_20201228_1243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='m10form',
            options={'verbose_name_plural': 'فورم م 10'},
        ),
        migrations.AlterModelOptions(
            name='m11form',
            options={'verbose_name_plural': 'فورم م 11'},
        ),
        migrations.AlterModelOptions(
            name='m3form',
            options={'verbose_name_plural': 'فورم م 3'},
        ),
        migrations.AlterModelOptions(
            name='m7form',
            options={'verbose_name_plural': 'فورم م 7'},
        ),
        migrations.AlterModelOptions(
            name='suggestionform',
            options={'verbose_name_plural': 'فورم پیشنهاد'},
        ),
        migrations.RemoveField(
            model_name='m7form',
            name='order_num',
        ),
        migrations.AlterField(
            model_name='m10form',
            name='amount',
            field=models.IntegerField(verbose_name='مبلغ'),
        ),
        migrations.AlterField(
            model_name='m10form',
            name='applicator',
            field=models.CharField(max_length=50, verbose_name='درخواست کننده'),
        ),
        migrations.AlterField(
            model_name='m10form',
            name='descript',
            field=models.CharField(max_length=100, verbose_name='موافقه تادیه'),
        ),
        migrations.AlterField(
            model_name='m10form',
            name='description',
            field=models.TextField(verbose_name='ضرورت پیشکی'),
        ),
        migrations.AlterField(
            model_name='m10form',
            name='issue_date',
            field=models.DateField(verbose_name='تاریخ منظوری'),
        ),
        migrations.AlterField(
            model_name='m10form',
            name='item_type',
            field=models.CharField(choices=[('SA', 'معاش'), ('PA', 'مسافرت'), ('PU', 'خریداری')], max_length=2, verbose_name='نوع پیشکی'),
        ),
        migrations.AlterField(
            model_name='m10form',
            name='suggestion_num',
            field=models.IntegerField(verbose_name='نمبر درخواستی'),
        ),
        migrations.AlterField(
            model_name='m11form',
            name='document_num',
            field=models.IntegerField(verbose_name='شماره مکتبوب'),
        ),
        migrations.AlterField(
            model_name='m11form',
            name='issued_date',
            field=models.DateField(verbose_name='تاریخ صدور'),
        ),
        migrations.AlterField(
            model_name='m11formdetail',
            name='dedicated',
            field=models.CharField(max_length=50, verbose_name='تهیه شده'),
        ),
        migrations.AlterField(
            model_name='m11formdetail',
            name='description',
            field=models.TextField(verbose_name='تشریحات'),
        ),
        migrations.AlterField(
            model_name='m11formdetail',
            name='expenses',
            field=models.IntegerField(verbose_name='مصارف'),
        ),
        migrations.AlterField(
            model_name='m3form',
            name='issued_date',
            field=models.DateField(verbose_name='تاریخ صدور'),
        ),
        migrations.AlterField(
            model_name='m3form',
            name='purchase_order_num',
            field=models.IntegerField(verbose_name='نمبر امر خریداری'),
        ),
        migrations.AlterField(
            model_name='m3form',
            name='purchase_suggestion_num',
            field=models.IntegerField(verbose_name='نمبر درخواست خریداری'),
        ),
        migrations.AlterField(
            model_name='m3form',
            name='suggestion_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input.suggestionform', verbose_name='شماره فورم پیشنهاد'),
        ),
        migrations.AlterField(
            model_name='m3formdetail',
            name='description',
            field=models.TextField(verbose_name='تشریحات'),
        ),
        migrations.AlterField(
            model_name='m3formdetail',
            name='item',
            field=models.CharField(max_length=30, verbose_name='جنس'),
        ),
        migrations.AlterField(
            model_name='m3formdetail',
            name='module',
            field=models.CharField(choices=[('P', 'قطی'), ('C', 'کارتن'), ('N', 'عدد')], max_length=1, verbose_name='فیات'),
        ),
        migrations.AlterField(
            model_name='m3formdetail',
            name='price',
            field=models.IntegerField(verbose_name='مجموع قیمت'),
        ),
        migrations.AlterField(
            model_name='m3formdetail',
            name='quantity',
            field=models.IntegerField(verbose_name='تعداد/دانه'),
        ),
        migrations.AlterField(
            model_name='m7form',
            name='issued_date',
            field=models.DateField(verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='m7form',
            name='purchase_place',
            field=models.CharField(default='بازار هرات', max_length=20, verbose_name='اخذ گردیده از'),
        ),
        migrations.AlterField(
            model_name='m7form',
            name='report_num',
            field=models.IntegerField(verbose_name='نمبر راپور'),
        ),
        migrations.AlterField(
            model_name='m7form',
            name='suggestion_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input.suggestionform', verbose_name='نمبر فرمایش'),
        ),
        migrations.AlterField(
            model_name='m7formdetail',
            name='description',
            field=models.TextField(verbose_name='تشریحات'),
        ),
        migrations.AlterField(
            model_name='m7formdetail',
            name='module',
            field=models.CharField(choices=[('P', 'قطی'), ('C', 'کارتن'), ('N', 'عدد')], max_length=1, verbose_name='واحد'),
        ),
        migrations.AlterField(
            model_name='m7formdetail',
            name='observations',
            field=models.CharField(max_length=60, verbose_name='ملاحظات'),
        ),
        migrations.AlterField(
            model_name='m7formdetail',
            name='quantity',
            field=models.IntegerField(verbose_name='مقدار'),
        ),
    ]
