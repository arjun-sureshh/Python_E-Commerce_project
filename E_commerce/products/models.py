from django.db import models

# Create your models here.

# Model for product
class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'Delete'))
    title=models.CharField(max_length=300)
    price=models.FloatField()
    descripton=models.TextField()
    images=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    def  __str__(self) -> str:
        return self.title