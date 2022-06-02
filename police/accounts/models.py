# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
category=(
        ('Male','MALE'),
        ('Female','FEMALE'),
        ('Other','OTHER'),
    )
marital_status=(
        ('single','SINGLE'),
        ('married','MARRIED'),
        ('divorced','DIVORCED'),
    )
logic=(
    ('yes','YES'),
    ('no','NO'),
)
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Qualification(models.Model):
    position=models.CharField(max_length=200,null=False)
    job_type=models.CharField(max_length=200,null=False)
    job_description=models.CharField(max_length=2000,null=False)
    reqiured_knowledge=models.CharField(max_length=2000,null=False)
    salary=models.CharField(max_length=2000,null=False)
    experience=models.CharField(max_length=2000,null=False)
    Deadline=models.CharField(max_length=2000,null=False,default='')
    status = models.IntegerField(choices=STATUS, default=0)
    

    

    def __str__(self):
        return self.position

class Candidates(models.Model):
    full_name=models.CharField(max_length=200,null=False)
    dob=models.DateField(null=False)
    gender= models.CharField(max_length=200,null=False,choices=category)
    country=models.CharField(max_length=200,null=False)
    marital_status= models.CharField(max_length=200,null=False,choices=marital_status)
    mobile= models.CharField(max_length=200,null=False)
    email= models.CharField(max_length=200,null=False)
    resume=models.FileField(null=False)
    position=models.ManyToManyField(Qualification,blank=False)
    do_you_have_serious_health_ailment=models.CharField(max_length=200,null=False,choices=logic)
    disability=models.CharField(max_length=200,null=False,choices=logic)
    do_you_use_hearing_aids=models.CharField(max_length=200,null=False,choices=logic)
    do_you_use_glasses_or_lenses_for_your_eyesight=models.CharField(max_length=200,null=False,choices=logic)
    have_you_beign_dependent_on_drugs_or_alcohol=models.CharField(max_length=200,null=False,choices=logic)
    

    def __str__(self):
        return self.full_name

class Contact(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    subject = models.CharField(max_length=100,null=True)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

