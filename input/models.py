from django.db import models

MODULE_CHOICES = (
    ('P', 'قطی'),
    ('C', 'کارتن'),
    ('N', 'عدد'),
)

M10FORM_ITEMTYPE_CHOICES = (
    ('SA', 'معاش'),
    ('PA', 'مسافرت'),
    ('PU', 'خریداری')
)


class SuggestionForm(models.Model):
    number = models.IntegerField(verbose_name="شماره")
    issued_date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name="تاریخ")
    deanship = models.CharField(
        max_length=100, verbose_name="مقام مربوطه", blank=True, null=True)
    department = models.CharField(
        max_length=100, verbose_name="ریاست مربوطه", blank=True, null=True)
    topic = models.CharField(
        max_length=100, verbose_name="موضوغ", blank=True, null=True)
    description = models.TextField(
        verbose_name="توضحات", blank=True, null=True)
    dean = models.CharField(
        max_length=30, verbose_name="اسم ریس", blank=True, null=True)
    dean_commandment = models.TextField(
        verbose_name="حکم ریس", blank=True, null=True)
    addminstartion_commandment = models.TextField(
        verbose_name="حکم بخش اداری", blank=True, null=True)
    advice_commitee = models.TextField(
        verbose_name="نظر هیت", blank=True, null=True)
    addminstration_final = models.TextField(
        verbose_name="اجرات بخش اداری", blank=True, null=True)

    class Meta:
        verbose_name = 'فورم پیشنهاد'
        verbose_name_plural = 'فورم پیشنهاد'

    def __str__(self):
        return str(self.number)


class M3Form(models.Model):
    suggestion_form = models.ForeignKey(
        SuggestionForm, on_delete=models.CASCADE, verbose_name="شماره فورم پیشنهاد", blank=True, null=True)
    purchase_order_num = models.IntegerField(
        verbose_name="نمبر امر خریداری", blank=True, null=True)
    issued_date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name="تاریخ صدور", blank=True, null=True)
    purchase_suggestion_num = models.IntegerField(
        verbose_name="نمبر درخواست خریداری", blank=True, null=True)

    class Meta:
        verbose_name = 'فورم 3'
        verbose_name_plural = 'فورم م 3'

    def __str__(self):
        return str(self.purchase_order_num)

    # description = models.TextField()
    # item = models.CharField(max_length=30)
    # quantity = models.IntegerField()
    # module = models.CharField(max_length=1, choices=MODULE_CHOICES)
    # price = models.IntegerField()


class M3FormDetail(models.Model):
    form = models.ForeignKey(M3Form, on_delete=models.CASCADE)
    description = models.TextField(
        verbose_name="تشریحات", blank=True, null=True)
    item = models.CharField(
        max_length=30, verbose_name="جنس", blank=True, null=True)
    quantity = models.IntegerField(
        verbose_name="تعداد/دانه", blank=True, null=True)
    module = models.CharField(
        max_length=1, choices=MODULE_CHOICES, verbose_name="فیات", blank=True, null=True)
    price = models.IntegerField(
        verbose_name="مجموع قیمت", blank=True, null=True)


class M7Form(models.Model):
    suggestion_form = models.ForeignKey(
        SuggestionForm, on_delete=models.CASCADE, verbose_name="نمبر فرمایش", blank=True, null=True)
    report_num = models.IntegerField(
        verbose_name="نمبر راپور", blank=True, null=True)
    issued_date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name="تاریخ", blank=True, null=True)
    # order_num = models.IntegerField(verbose_name="شماره")
    purchase_place = models.CharField(
        max_length=20, default="بازار هرات", verbose_name="اخذ گردیده از", blank=True, null=True)

    class Meta:
        verbose_name = 'فورم 7'
        verbose_name_plural = 'فورم م 7'

    def __str__(self):
        return str(self.report_num)


class M7FormDetail(models.Model):
    form = models.ForeignKey(M7Form, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="مقدار", blank=True, null=True)
    module = models.CharField(
        max_length=1, choices=MODULE_CHOICES, verbose_name="واحد", blank=True, null=True)
    description = models.TextField(
        verbose_name="تشریحات", blank=True, null=True)
    fiyat = models.IntegerField(verbose_name="فیات", blank=True, null=True)
    amount = models.IntegerField(verbose_name="مبلغ", blank=True, null=True)
    observations = models.CharField(
        max_length=60, verbose_name="ملاحظات", blank=True, null=True)


class M11Form(models.Model):
    document_num = models.IntegerField(
        verbose_name="شماره مکتبوب", blank=True, null=True)
    issued_date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name="تاریخ صدور", blank=True, null=True)

    class Meta:
        verbose_name = 'فورم 11'
        verbose_name_plural = 'فورم م 11'

    def __str__(self):
        return str(self.document_num)


class M11FormDetail(models.Model):
    form = models.ForeignKey(
        M11Form, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(
        verbose_name="تشریحات", blank=True, null=True)
    expenses = models.IntegerField(verbose_name="مصارف", blank=True, null=True)
    dedicated = models.CharField(
        max_length=50, verbose_name="تهیه شده", blank=True, null=True)

    class Meta:
        verbose_name = 'فورم 11'
        verbose_name_plural = 'فورم م 11'


class M10Form(models.Model):
    suggestion_num = models.IntegerField(
        verbose_name="نمبر درخواستی", blank=True, null=True)
    issue_date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name="تاریخ منظوری", blank=True, null=True)
    applicator = models.CharField(
        max_length=50, verbose_name="درخواست کننده", blank=True, null=True)  # check data type
    amount = models.IntegerField(verbose_name="مبلغ", blank=True, null=True)
    item_type = models.CharField(
        max_length=2, choices=M10FORM_ITEMTYPE_CHOICES, verbose_name="نوع پیشکی", blank=True, null=True)
    descript = models.CharField(
        max_length=100, verbose_name="موافقه تادیه", blank=True, null=True)
    description = models.TextField(
        verbose_name="ضرورت پیشکی", blank=True, null=True)

    class Meta:
        verbose_name = 'فورم 10'
        verbose_name_plural = 'فورم م 10'

    def __str__(self):
        return str(self.suggestion_num)
