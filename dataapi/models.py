from django.db import models

# Create your models here.

class biddetail(models.Model):
  ''' the detail of bids '''
  biddername = models.CharField(max_length=128)
  bidderprice = models.IntegerField()



class Bidslist(models.Model):
  ''' BidList '''
  name = models.CharField(max_length=128)
  winner = models.CharField(max_length=128)
