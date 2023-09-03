from django.contrib.auth.models import User
from django.db import models
import uuid



    

class APIKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.key)
    
    
class UserDetails(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=50, default="")
    phoneNum = models.CharField(max_length=50, default="")
    userPlan = models.CharField(max_length=50, default="")
    userPlanStartDate = models.CharField(max_length=50, default="")
    userApiKey =  models.CharField(max_length=50, default="")
    userDailyLimitServerRequests = models.IntegerField(default=0)
    userDailyLimitChatRequests = models.IntegerField(default=0)
    userDailyLimitRecRequests = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)
    
class UserDayCount(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.CharField(max_length=50, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userDayCountServerRequests = models.IntegerField(default=0)
    userDayCountChatRequests = models.IntegerField(default=0)
    userDayCountRecRequests = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)


class StoreData(models.Model):
    user = models.CharField(max_length=50, default="")
    nitrogen = models.IntegerField(default=0)
    phosphorus = models.IntegerField(default=0)
    potassium = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    temperature = models.IntegerField(default=0)
    soil_moisture = models.IntegerField(default=0)
    # ph = models.IntegerField(default=0)
    ph = models.FloatField(default=0.0)
    state = models.CharField(max_length=50)
    rainfall = models.IntegerField(default=0)
    season = models.CharField(max_length=50)
    # timestamp = models.DateTimeField(auto_now_add=True)
    dateStamp = models.CharField(max_length=50, default="")
    timeStamp = models.CharField(max_length=50, default="")

    def __str__(self):
        return str(self.user)
    
    

class pricingmodel(models.Model):

    # only monthly
    pri_planName = models.CharField(max_length=50, default="")    
    
    pri_Monthly_price = models.CharField(max_length=50, default="")    
    pri_Monthly_slug = models.CharField(max_length=80, default="")

    pri_Annually_price = models.CharField(max_length=50, default="")    
    pri_Annually_slug = models.CharField(max_length=80, default="")    
    
    pri_detailslist = models.CharField(max_length=5000, default="")    

    def __str__(self):
        return self.pri_planName
    

# commented
'''
# # Create your models here.
# class alldata(models.Model):
#     dataid = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=50)
#     category = models.CharField(max_length=50, default="")
#     slug = models.CharField(max_length=100, default="")
#     price = models.IntegerField(default=0)
    
#     desc = models.CharField(max_length=300)
#     image = models.ImageField(upload_to="tze/images", default="")
#     testimoniallink = models.CharField(max_length=300, default="")
#     ytlink = models.CharField(max_length=300, default="")
#     benifits = models.CharField(max_length=300, default="")
#     how_to_use = models.CharField(max_length=400, default="")
#     doc_link = models.CharField(max_length=300, default="")
#     net_Qty = models.CharField(max_length=100, default="")
#     pack_of = models.CharField(max_length=50, default="")
#     # pub_date = models.DateField()
#     # subcategory = models.CharField(max_length=30, default="")

#     def __str__(self):
#         return self.product_name

'''