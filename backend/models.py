from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

class Member(models.Model):
    mId = models.AutoField(db_column="mId", primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    birthday = models.DateField()
    credit_card = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    ssn = models.CharField(max_length=255)
    
    class Meta:
        db_table = "Member"

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
    
class Product(models.Model):
    pId = models.AutoField(db_column='pId', primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    brand = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    likes = models.IntegerField()
    state = models.CharField(max_length=255)

    class Meta:
        db_table = "Product"

class Picture(models.Model):
    pId = models.ForeignKey(Product, models.CASCADE, db_column="pId", primary_key=True)
    picture = models.CharField(max_length=255)

    class Meta:
        db_table= "Picture"
        unique_together = ('pId', 'picture')

class Orders(models.Model):
    oId = models.AutoField(db_column='oId', primary_key=True)
    mId = models.ForeignKey(Member, models.CASCADE, db_column="mId", null=True)
    pId = models.ForeignKey(Product, models.CASCADE, db_column="pId", null=True)
    payment = models.CharField(max_length=255)
    order_time = models.DateTimeField()
    duration = models.IntegerField()
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    startTime = models.DateField(db_column='startTime')
    endTime = models.DateField(db_column='endTime')
    
    class Meta:
        db_table = "Orders"

class Comment(models.Model):
    pId = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="pId")
    mId = models.ForeignKey(Member, on_delete=models.CASCADE, db_column="mId")
    cId = models.AutoField(primary_key=True)
    content = models.CharField(max_length=255)
    rank = models.IntegerField()

    class Meta:
        db_table = 'Comment'

class Cart(models.Model):
    pId = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="pId", primary_key=True)
    mId = models.ForeignKey(Member, on_delete=models.CASCADE, db_column="mId")
    cartTime = models.DateTimeField(db_column="cartTime")
    startTime = models.DateField(db_column="startTime")
    endTime = models.DateField(db_column="endTime")
    
    class Meta:
        db_table = 'Cart'
        unique_together = ('mId', 'pId')