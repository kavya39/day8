from django.db import models
from django.contrib.auth.models import User,AbstractUser
from datetime import date

class User(AbstractUser):
	t = (
		(1,'Customer'),
		(2,'Shopkeeper'),
		(3,'Anonymous'),
		)
	role = models.IntegerField(default=3,choices=t)

class HandiCrafts(models.Model):
	a=[('Fashion',"fashion"),('Toys',"Toys"),('Decor',"Decor")]
	category_type=models.CharField(max_length=10,choices=a)
	im=models.ImageField(upload_to='handcrafts/',default='b.jpg')
	quantity=models.IntegerField()
	price=models.DecimalField(max_digits=6,decimal_places=2)
	da = models.DateField(auto_now_add=True)
	uid=models.ForeignKey(User,on_delete=models.CASCADE)

class Worker(models.Model):
	a=[('Artisan',"Artisan"),('Weaver',"Weaver")]
	profession=models.CharField(max_length=10,choices=a)
	name=models.CharField(max_length=20)
	phno=models.IntegerField()
	b=[('male',"Male"),('female',"Female")]
	gender=models.CharField(max_length=20,choices=b)
	Email=models.EmailField(max_length=100)

class Category(models.Model):
	cname=models.CharField(max_length=20)
	def __str__(self):
		return self.cname

class Product(models.Model):
	pname=models.CharField(max_length=30)
	price=models.IntegerField()
	im=models.ImageField()
	pid=models.ForeignKey(Category,on_delete=models.CASCADE)
	def __str__(self):
		return self.pname



