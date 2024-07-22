from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()
class Profile(models.Model):
    user = models.ForeignKey( User , on_delete=models.CASCADE)
    # username = models.CharField(max_length = 100)
    user_type = models.CharField(max_length = 100, blank = True, null = True , default = "player")
    #first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    # email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='dps',default='user.png',blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    COACH_CHOICES = [
        ('cricket', 'Cricket_coach'),
        ('football', 'Football_coach'),
        ('goalkeeping_coach', 'Goalkeeping Coach'),
        ('fitness_coach', 'Fitness Coach'),
        # Add more choices as needed
    ]
    coach_type = models.CharField(max_length=20, choices=COACH_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
# class coach(models.Model):
#     username = models.CharField(max_length = 100)
#     coach_name = models.CharField(max_length = 100)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     coach_email = models.CharField(unique = True)
#     contact_no = models.IntegerField(blank=True,null=True)
#     experience = models.IntegerField(blank = True , null = True)

#     def __str__(self):
#         return self.user.username
    
class Sport(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='sport_img',default='user.png',blank=True,null=True)
    description = models.CharField(max_length = 1000)


class Event(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='sport_img',default='user.png',blank=True,null=True)
    description = models.CharField(max_length = 1000)
    date = models.DateTimeField()


class EventParticipation(models.Model):
    event = models.ForeignKey(Event ,on_delete=models.CASCADE)
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    date = models.DateTimeField()
    

class Messages(models.Model):
    sender = models.ForeignKey( User , on_delete=models.CASCADE )
    reciever = models.ForeignKey( User, on_delete=models.CASCADE, related_name="Messages")
    message = models.TextField()
    date = models.DateTimeField()





    
    
