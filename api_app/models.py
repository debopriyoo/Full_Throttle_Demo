from django.db import models

# Create your models here.
class People(models.Model):
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    # id = models.IntegerField(primary_key=True)
    real_name = models.CharField(max_length=128)
    tz = models.CharField(max_length=32, choices= TIMEZONES, default='UTC')
    im = models.CharField(max_length=28,unique=True)

    def __str__(self):
        return self.im

# TODO : Table name against class

class ActivityPeriod(models.Model):
    # activityid = models.IntegerField(primary_key=True)
    im = models.ForeignKey(People,on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    #def __str__(self):
        #return self.activityid
