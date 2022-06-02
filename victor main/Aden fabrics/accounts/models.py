from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


Status = (
    ('processing', 'PROCESSING'),
    ('collected', 'COLLECTED'),  
)


class Employee(models.Model):
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=400,null=False)
    job_type=models.CharField(max_length=100,null=False,default='')
    lga=models.CharField(max_length=200,null=False)
    state=models.CharField(max_length=200,null=False)
    phone_no=models.CharField(max_length=11,null=False)
    date_of_appointment=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class Customer(models.Model):
    full_name=models.CharField(max_length=100,null=True)
    service_render=models.CharField(max_length=100,null=False)
    cloth_type=models.TextField(max_length=100,null=False)
    total_number_of_cloth=models.CharField(max_length=100,null=False)
    amount_charged=models.CharField(max_length=100,null=False)
    status=models.CharField(max_length=200,null=False, default='', choices=Status)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Report(models.Model):
    total_income_for_today=models.CharField(max_length=200,null=False)
    total_profit_for_today=models.CharField(max_length=200,null=False)
    total_expenditure_today=models.CharField(max_length=200,null=False,default='')
    total_laundry_claimed_today=models.CharField(max_length=200,null=False)
    total_customer_today=models.CharField(max_length=200,null=False)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.total_income_for_today

class Inventory(models.Model):
    name=models.CharField(max_length=200,null=False)
    quantity=models.CharField(max_length=200,null=False)
    


    def __str__(self):
        return self.name