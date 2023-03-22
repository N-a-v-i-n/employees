from django.db import models

# Create your models here.
class department(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class roles(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    email_id=models.CharField(max_length=100)
    # dept=models.ForeignKey(department,on_delete=models.CASCADE)
    dept=models.CharField(max_length=100)
    # role=models.ForeignKey(roles,on_delete=models.CASCADE)
    role=models.CharField(max_length=100)
    hire_date=models.DateField()
    def __str__(self):
        return f"{self.first_name}"

class otp_verifing(models.Model):
    otp_sent_mail=models.CharField(max_length=30)
    otp_sent=models.IntegerField()

    def __str__(self):
        return f"{self.otp_sent_mail}"




