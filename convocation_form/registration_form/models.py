from django.db import models

class Applicant(models.Model):
    # Personal Information
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])

    # Contact Information
    permanent_address = models.TextField()
    present_address = models.TextField()
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField()

    # Degree Information
    id_no =models.CharField(max_length=10)
    degree_name = models.CharField(max_length=20)
    admission_session = models.CharField(max_length=20)
    passing_year = models.DateField()
    cgpa = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.id_no} -- {self.name} "
