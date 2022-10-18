from django.db import models

# Create your models here.
class Sale_data(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField()
    time=models.TimeField()
    customer_name=models.CharField(max_length=100)
    customer_address=models.CharField(max_length=100)
    customer_zipcode=models.CharField(max_length=100)
    customer_phone=models.CharField(max_length=100)
    customer_email=models.CharField(max_length=100)
    screenshot=models.ImageField(upload_to='images/')
    STATUS=(('Pending','Pending'),('Done','Done'),('Reschedule','Reschedule'),('Cancel','Cancel'))
    status=models.CharField(max_length=100,choices=STATUS)
    def __str__(self):
        return self.customer_name+self.customer_email+self.customer_phone+self.customer_address+self.customer_zipcode



