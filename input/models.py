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
    number = models.IntegerField()
    issued_date = models.DateField(auto_now=False, auto_now_add=False)
    deanship = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    description = models.TextField()
    dean = models.CharField(max_length=30)
    dean_commandment = models.TextField()
    addminstartion_commandment = models.TextField()
    advice_commitee = models.TextField()
    addminstration_final = models.TextField()


class M3Form(models.Model):
    suggestion_form = models.ForeignKey(SuggestionForm, on_delete=models.CASCADE)
    purchase_order_num = models.IntegerField() 
    issued_date = models.DateField(auto_now=False, auto_now_add=False)
    purchase_suggestion_num = models.IntegerField() 


class M3FormDetail(models.Model):
    form = models.ForeignKey(M3Form, on_delete=models.CASCADE)
    description = models.TextField() 
    item = models.CharField(max_length=30)
    quantity = models.IntegerField()
    module = models.CharField(max_length=1, choices=MODULE_CHOICES) 
    price = models.IntegerField()


class M7Form(models.Model):
    suggestion_form = models.ForeignKey(SuggestionForm, on_delete=models.CASCADE)
    report_num = models.IntegerField()
    issued_date = models.DateField(auto_now=False, auto_now_add=False)
    order_num = models.IntegerField()
    purchase_place = models.CharField(max_length=20, default="بازار هرات")


class M7FormDetail(models.Model):
    form = models.ForeignKey(M7Form, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    module = models.CharField(max_length=1, choices=MODULE_CHOICES)
    description = models.CharField(max_length=100)
    observations = models.CharField(max_length=60)

class M11Form(models.Model):
    document_num = models.IntegerField() 
    issued_date = models.DateField(auto_now=False, auto_now_add=False)


class M11FormDetail(models.Model):
    form = models.ForeignKey(M11Form, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    expenses = models.IntegerField()
    dedicated = models.CharField(max_length=50)


class M10Form(models.Model):
    suggestion_num = models.IntegerField()
    issue_date = models.DateField(auto_now=False, auto_now_add=False)
    applicator = models.CharField(max_length=50)  #check data type 
    item_type  = models.CharField(max_length=2, choices=M10FORM_ITEMTYPE_CHOICES)
    amount = models.IntegerField()
    descript = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

