from django.db import models
import uuid 
from .choices import *
class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
        
class Services(BaseModel):
    it_infrastructure = models.CharField(max_length = 100)
    storage_n_backup = models.CharField(max_length = 100)
    cctv_surveillance = models.CharField(max_length = 100)
    civil_works = models.CharField(max_length = 100)
    application_n_platforms = models.CharField(max_length = 100)
    cybersecurity_n_network = models.CharField(max_length = 100)
    cloud_n_virtualization_services = models.CharField(max_length = 100)
    Electrical_works = models.CharField(max_length = 100)
    
class Product(BaseModel):
    product_choices = models.CharField(max_length=100,choices=product_choices)
    description = models.TextField(max_length=500)
    
class Dept_type(BaseModel):
    engg = models.CharField(max_length=100,choices=dept_choices)
    department = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 100)
    job_location = models.CharField(max_length = 100)
    job_description = models.CharField(max_length = 100)
    
class Offices(BaseModel):
    office_choices = models.CharField(max_length=100,choices=office_choices)
    address = models.TextField(max_length=500)
    
class Contact_us(BaseModel):
    full_name = models.CharField(max_length = 100)
    phone_no = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 100)
    message = models.TextField(max_length = 200)
    
class Industries(BaseModel):
    government_enterprises = models.CharField(max_length = 100) 
    hospitality_info = models.CharField(max_length = 100) 
    production_of_goods = models.CharField(max_length = 100) 
    telecommunications = models.CharField(max_length = 100) 
    building_construction = models.CharField(max_length = 100) 
    power_n_energy = models.CharField(max_length = 100) 
    
class Career(BaseModel):
    category = models.CharField(max_length=100,choices=ch)
    designation = models.CharField(max_length = 100) 
    job_location = models.CharField(max_length = 100) 
    job_description = models.TextField(max_length = 500) 
    
    
    

    
    
    
    
    