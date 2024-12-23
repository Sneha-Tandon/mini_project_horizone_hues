from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.core.validators import RegexValidator, EmailValidator
from django.utils import timezone
import datetime

class TouristManager(BaseUserManager):
    def create_user(self, email, fname, lname, phone_number, pass1, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, fname=fname, lname=lname, phone_number=phone_number, **extra_fields)
        user.set_password(pass1)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fname=None, lname=None, phone_number=None, pass1=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, fname, lname, phone_number, pass1, **extra_fields)
    



class Tourist(AbstractUser):
    fname=models.CharField(max_length=30,null=True,default=None)
    lname=models.CharField(max_length=30,null=True,default=None)
    email = models.EmailField(validators=[EmailValidator(message="Enter a valid email address.")],null=True,default=None)
    phone_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits.")],null=True,default=None
    )
    pass1=models.CharField(max_length=20,null=True,default=None)
    date=models.DateField(default="2022-01-01")
    
    objects = TouristManager()
    
    def __str__(self):
        return f"{self.fname} {self.lname} {self.email}"
    

class Package(models.Model):
    package_id=models.AutoField(primary_key=True)
    # this is the raor pay attributes that I have added
    # razor_pay_order_id=models.CharField(max_length=100,null=True,blank=True)
    # razor_pay_payment_id=models.CharField(max_length=100,null=True,blank=True)
    # razor_pay_payment_signature=models.CharField(max_length=100,null=True,blank=True)
    location= models.CharField(max_length=100,null=True,default=None)
    description=models.CharField(max_length=1000,null=True,default=None)
    image=models.CharField(max_length=2000,null=True,default=None)
    group=models.CharField(max_length=1000,null=True,default=None)
    prev_price=models.IntegerField(null=True,default=None)
    discount=models.IntegerField(null=True,default=None)
    discounted_price=models.IntegerField(null=True,default=None,blank=True)
    nights=models.IntegerField(null=True,default=None)
    days=models.IntegerField(null=True,default=None)

    
    def __str__(self):
        return f"{self.package_id} {self.location}"
    
    def save(self, *args, **kwargs):
        # Calculate discounted price before saving
        if self.prev_price is not None and self.discount is not None:
            self.discounted_price = self.prev_price - (self.prev_price * (self.discount / 100))
        super(Package, self).save(*args, **kwargs)
    
class Hotel(models.Model):
    Hotel_id=models.AutoField(primary_key=True)
    location= models.CharField(max_length=100,null=True,default=None)
    description=models.CharField(max_length=1000,null=True,default=None)
    image=models.CharField(max_length=2000,null=True,default=None)
    group=models.CharField(max_length=1000,null=True,default=None)
    prev_price=models.IntegerField(null=True,default=None)
    discount=models.IntegerField(null=True,default=None)
    discounted_price=models.IntegerField(null=True,default=None,blank=True)
    
    def str(self):
        return f"{self.Hotel_id} {self.location}"
    
    def save(self, *args, **kwargs):
        # Calculate discounted price before saving
        if self.prev_price is not None and self.discount is not None:
            self.discounted_price = self.prev_price - (self.prev_price * (self.discount / 100))
        super(Hotel, self).save(*args,**kwargs)
    
    


class Buy_now(models.Model):
    package_id=models.IntegerField(null=True,default=None)
    location= models.CharField(max_length=100,null=True,default=None)
    image1=models.CharField(max_length=2000,null=True,default=None)
    image2=models.CharField(max_length=2000,null=True,default=None)
    image3=models.CharField(max_length=2000,null=True,default=None)
    image4=models.CharField(max_length=2000,null=True,default=None)
    activity1=models.CharField(max_length=1000,null=True,default=None)
    activity2=models.CharField(max_length=1000,null=True,default=None)
    activity3=models.CharField(max_length=1000,null=True,default=None)
    activity4=models.CharField(max_length=1000,null=True,default=None)
    activity5=models.CharField(max_length=5000,null=True,default=None)
    itenary1=models.CharField(max_length=5000,null=True,default=None)
    itenary2=models.CharField(max_length=5000,null=True,default=None)
    itenary3=models.CharField(max_length=5000,null=True,default=None)
    itenary4=models.CharField(max_length=5000,null=True,default=None)
    itenary_image1=models.CharField(max_length=2000,null=True,default=None)
    itenary_image2=models.CharField(max_length=2000,null=True,default=None)
    itenary_image3=models.CharField(max_length=2000,null=True,default=None)
    itenary_image4=models.CharField(max_length=2000,null=True,default=None)
    def __str__(self):
        return f"{self.package_id} {self.location}"
    

class MyCart(models.Model):
    cart_id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=50,null=True,default=None)
    package_id=models.IntegerField(null=True,default=None)
    location= models.CharField(max_length=100,null=True,default=None)
    description=models.CharField(max_length=1000,null=True,default=None)
    image=models.CharField(max_length=2000,null=True,default=None)
    group=models.CharField(max_length=1000,null=True,default=None)
    prev_price=models.IntegerField(null=True,default=None)
    discount=models.IntegerField(null=True,default=None)
    discounted_price=models.IntegerField(null=True,default=None,blank=True)
    nights=models.IntegerField(null=True,default=None)
    days=models.IntegerField(null=True,default=None)
    
    def __str__(self):
        return f"{self.cart_id} {self.package_id} {self.location}"
    
class Feedback(models.Model):
    sno=models.AutoField(primary_key=True,default=0)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    review=models.TextField()
    suggestion=models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}" 
    

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_date = models.DateField(default=datetime.date.today)
    fname=models.CharField(max_length=30,null=True,default=None)
    lname=models.CharField(max_length=30,null=True,default=None)    
    email=models.CharField(max_length=50,null=True,default=None)
    phone=models.CharField(max_length=100,null=True,default=None)
    package_id=models.IntegerField(null=True,default=None)
    location= models.CharField(max_length=100,null=True,default=None)
    image=models.CharField(max_length=2000,null=True,default=None)
    group=models.CharField(max_length=1000,null=True,default=None)
    prev_price=models.IntegerField(null=True,default=None)
    discount=models.IntegerField(null=True,default=None)
    discounted_price=models.IntegerField(null=True,default=None,blank=True)
    nights=models.IntegerField(null=True,default=None)
    days=models.IntegerField(null=True,default=None)
    checkin_date=models.CharField(max_length=30,null=True,default=None)
    checkout_date=models.CharField(max_length=30,null=True,default=None)

    def __str__(self):
        return f"{self.fname} {self.email} {self.location}"
    
class Home(models.Model):
    C_Image=models.CharField(max_length=2000,null=True,default=None)
    C_Caption=models.CharField(max_length=100,null=True,default=None)

    C_Image2=models.CharField(max_length=2000,null=True,default=None)
    C_Caption2=models.CharField(max_length=100,null=True,default=None)

    C_Image3=models.CharField(max_length=2000,null=True,default=None)
    C_Caption3=models.CharField(max_length=100,null=True,default=None)

    s_id=models.AutoField(primary_key=True)
    Package_id=models.IntegerField(primary_key=False,null=True,default=None)
    Location=models.CharField(max_length=100,null=True,default=None)
    Description=models.CharField(max_length=100,null=True,default=None)
    Image=models.CharField(max_length=2000,null=True,default=None)
    Price=models.CharField(max_length=1000,null=True,default=None)

    Package_id2=models.IntegerField(primary_key=False,null=True,default=None)
    Location2=models.CharField(max_length=100,null=True,default=None)
    Description2=models.CharField(max_length=100,null=True,default=None)
    Image2=models.CharField(max_length=2000,null=True,default=None)
    Price2=models.CharField(max_length=1000,null=True,default=None)


    Package_id3=models.IntegerField(primary_key=False,null=True,default=None)
    Location3=models.CharField(max_length=100,null=True,default=None)
    Description3=models.CharField(max_length=100,null=True,default=None)
    Image3=models.CharField(max_length=2000,null=True,default=None)
    Price3=models.CharField(max_length=1000,null=True,default=None)

    Package_id4=models.IntegerField(primary_key=False,null=True,default=None)
    Location4=models.CharField(max_length=100,null=True,default=None)
    Description4=models.CharField(max_length=100,null=True,default=None)
    Image4=models.CharField(max_length=2000,null=True,default=None)
    Price4=models.CharField(max_length=1000,null=True,default=None)

    Package_id5=models.IntegerField(primary_key=False,null=True,default=None)
    Location5=models.CharField(max_length=100,null=True,default=None)
    Description5=models.CharField(max_length=100,null=True,default=None)
    Image5=models.CharField(max_length=2000,null=True,default=None)
    Price5=models.CharField(max_length=1000,null=True,default=None)

    Hotel_id=models.IntegerField(primary_key=False,null=True,default=None)
    H_City=models.CharField(max_length=100,null=True,default=None)
    H_Description=models.CharField(max_length=1000,null=True,default=None)
    H_Image=models.CharField(max_length=2000,null=True,default=None)
    H_Price=models.CharField(max_length=100,null=True,default=None)

    Hotel_id2=models.IntegerField(primary_key=False,null=True,default=None)
    H_City2=models.CharField(max_length=100,null=True,default=None)
    H_Description2=models.CharField(max_length=1000,null=True,default=None)
    H_Image2=models.CharField(max_length=2000,null=True,default=None)
    H_Price2=models.CharField(max_length=100,null=True,default=None)

    Hotel_id3=models.IntegerField(primary_key=False,null=True,default=None)
    H_City3=models.CharField(max_length=100,null=True,default=None)
    H_Description3=models.CharField(max_length=1000,null=True,default=None)
    H_Image3=models.CharField(max_length=2000,null=True,default=None)
    H_Price3=models.CharField(max_length=100,null=True,default=None)

    Hotel_id4=models.IntegerField(primary_key=False,null=True,default=None)
    H_City4=models.CharField(max_length=100,null=True,default=None)
    H_Description4=models.CharField(max_length=1000,null=True,default=None)
    H_Image4=models.CharField(max_length=2000,null=True,default=None)
    H_Price4=models.CharField(max_length=100,null=True,default=None)

    Hotel_id5=models.IntegerField(primary_key=False,null=True,default=None)
    H_City5=models.CharField(max_length=100,null=True,default=None)
    H_Description5=models.CharField(max_length=1000,null=True,default=None)
    H_Image5=models.CharField(max_length=2000,null=True,default=None)
    H_Price5=models.CharField(max_length=100,null=True,default=None)
    

