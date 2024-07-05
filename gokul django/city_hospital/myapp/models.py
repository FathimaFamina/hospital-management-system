from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_desc=models.TextField()
    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_image=models.ImageField()
    dep_name=models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_spec=models.CharField(max_length=100)

    def __str__(self):
        return self.doc_name + ' -(' + self.doc_spec + ')'

class Appointment(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.p_name} with {self.doc_name} on {self.booking_date}"

