# rws_app/models.py
from django.db import models
from django.db.models import Sum
from django.utils import timezone # <-- Add this import for date defaults
from decimal import Decimal

# This model stores the main work/project details.
class Work(models.Model):
    # FIX: Added default='' to all CharFields
    name = models.CharField(max_length=255, default='', verbose_name="Name of Work")
    order_details = models.CharField(max_length=255, default='', unique=True, verbose_name="Work Order Date Year & Commencement")
    
    # FIX: Ensured all DecimalFields have a default
    tender_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0, verbose_name="Amount of the Works to Tender")
    emd_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="EMD Amount")
    work_order_sd = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Work Order SD")
    add_sd = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Add. SD")

    def __str__(self):
        return self.name

# This model stores the individual bills associated with a Work.
class Bill(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='bills')
    
    # FIX: Added a default for the DateField and CharField
    bill_date = models.DateField(default=timezone.now, verbose_name="Bill Date")
    bill_no = models.CharField(max_length=100, default='', verbose_name="Bill No.")
    
    taxable_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Taxable Amt")
    gst = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="GST")
    
    # All deduction fields already had defaults, which is good.
    sd_deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Deduction: SD")
    it_deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Deduction: IT")
    gst_2_deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Deduction: GST 2%")
    insurance_deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Deduction: Insurance")
    cess_deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Deduction: Cess")
    royalty_deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Deduction: Royalty")
    fine_deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Deduction: Fine")
    other_deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Deduction: Other")
    
    financial_year = models.CharField(max_length=20, default='', verbose_name="Year")

    @property
    def total_bill_amount(self):
        return self.taxable_amount + self.gst

    @property
    def deduction_total(self):
        return (self.sd_deduction + self.it_deduction + self.gst_2_deduction + self.insurance_deduction + 
                self.cess_deduction + self.royalty_deduction + self.fine_deduction + self.other_deduction)

    @property
    def cheque_amount(self):
        return self.total_bill_amount - self.deduction_total

    def __str__(self):
        return f"{self.bill_no} for {self.work.name}"