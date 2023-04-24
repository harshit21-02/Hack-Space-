from django.db import models
from django.utils import timezone
import math
# # Create your models here.

class submission(models.Model):
    id = models.AutoField('id',primary_key=True)
    flag=models.BooleanField('flag')
    pub_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)
    Title=models.CharField('title',blank=False,max_length=200)
    Summary=models.CharField('summary',blank=True,max_length=500)
    Description=models.TextField('summary',blank=True)
    Hackathon_name=models.CharField('hackathonname',blank=False,max_length=200)
    Hackathon_startdate=models.DateField('hackathonstartdate',blank=False)
    Hackathon_enddate=models.DateField('hackathonenddate',blank=False)
    Github=models.URLField('github')
    Other=models.URLField('others',blank=True)
    image=models.ImageField(upload_to="", default=None)

    def __str__(self):
        return self.Title

    def whenpublished(self):
       now = timezone.now()
       
       diff= now - self.pub_date
       if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
           seconds= diff.seconds
           
           if seconds == 1:
               return "uploaded " + str(seconds) +  "second ago"
           
           else:
               return "uploaded " + str(seconds) + " seconds ago"
           
       if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
           minutes= math.floor(diff.seconds/60)
           if minutes == 1:
               return "uploaded " + str(minutes) + " minute ago"
           
           else:
               return "uploaded " + str(minutes) + " minutes ago"
       if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
           hours= math.floor(diff.seconds/3600)
           if hours == 1:
               return "uploaded " + str(hours) + " hour ago"
           else:
               return "uploaded " + str(hours) + " hours ago"
       # 1 day to 30 days
       if diff.days >= 1 and diff.days < 30:
           days= diff.days
       
           if days == 1:
               return "uploaded " + str(days) + " day ago"
           else:
               return "uploaded " + str(days) + " days ago"
       if diff.days >= 30 and diff.days < 365:
           months= math.floor(diff.days/30)
           
           if months == 1:
               return "uploaded " + str(months) + " month ago"
           else:
               return "uploaded " + str(months) + " months ago"
       if diff.days >= 365:
           years= math.floor(diff.days/365)
           if years == 1:
               return "uploaded " + str(years) + " year ago"
           else:
               return "uploaded " + str(years) + " years ago"
