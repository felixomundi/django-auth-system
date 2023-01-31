# from email import message
# from email.policy import default
# from pickle import FALSE
# from django.db import models
# from django.contrib.auth.models import User
# from tinymce.models import HTMLField
# from decimal import Decimal
# import os

    
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)   
#     phone = models.CharField(max_length=200, null=False)
#     address1 = models.CharField(max_length=200, null=False)
#     address2 = models.CharField(max_length=200, null=False)
#     country = models.CharField(max_length=200, null=False)
#     city = models.CharField(max_length=200, null=False)
#     state = models.CharField(max_length=200, null=False)
#     zipcode = models.CharField(max_length=200, null=False)   
#     profile_image = models.ImageField(upload_to="customer_profile_images") 
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return str(self.user.username)


# class Product(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     price = models.DecimalField(max_digits=7, decimal_places=2)
#     quantity =models.IntegerField()
#     offer_price = models.DecimalField(max_digits=7, decimal_places=2)    
#     image = models.ImageField(null=True, blank=True, upload_to="products")
#     description = HTMLField(max_length=30000000, null=True, blank=True)
#     status = models.BooleanField(default=True)
    
#     class Meta:
#         ordering = ['-id']

#     def __str__(self):
#         return str(self.name)

#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = 'https://drive.google.com/uc?id=1GqPCG4lqV_mDVe17i3yxMQCPWOcTBPT5'
#         return url
    
# class Cart(models.Model): 
#     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     product_qty = models.IntegerField()
#     purchased = models.BooleanField(default=False)
#     date_added = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
    
# class Order(models.Model):
#       user = models.ForeignKey(User, on_delete=models.CASCADE)
#       first_name =  models.CharField(max_length=200, null=False)
#       last_name =  models.CharField(max_length=200, null=False)
#       email =  models.EmailField(max_length=200, null=False)
#       phone =  models.CharField(max_length=200, null=False)
#       address1 =  models.CharField(max_length=200, null=False)
#       address2 =  models.CharField(max_length=200, null=False)
#       country =  models.CharField(max_length=200,null=False)
#       city =  models.CharField(max_length=200, null=False)
#       state =  models.CharField(max_length=200, null=False)
#       zipcode = models.CharField(max_length=200, null=False)
#       total_price = models.FloatField(null=False)
#       payment_mode =models.CharField(max_length=200,null=False)
#       payment_id = models.CharField(max_length=300,null=True)
#       orderstatuses = (
#           ('Pending','Pending'),
#           ('Out for shipping','Out for shipping'),
#           ('Completed','Completed')
          
#       )
#       status=models.CharField(max_length=40, choices=orderstatuses,default='Pending')
#       message = models.TextField(null=True)
#       tracking_number = models.CharField(max_length=150, null=True)
#       created = models.DateTimeField(auto_now_add=True)
#       updated = models.DateTimeField(auto_now=True)
      
#       def __str__(self):
#             return '{} - {}'.format(self.id, self.tracking_number)
        
        

# class OrderItem(models.Model):
#       order = models.ForeignKey(Order, on_delete=models.CASCADE)
#       product = models.ForeignKey(Product, on_delete=models.CASCADE)
#       price = models.FloatField(null=False)
#       quantity = models.IntegerField(null=False)
      
#       def __str__(self):
#             return '{}  {}'.format(self.order.id,self.order.tracking_number)
        
    
          
# class Contact(models.Model):
#     email=models.EmailField()
#     phone = models.CharField(max_length=40)
#     address = models.CharField(max_length=150)    
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)