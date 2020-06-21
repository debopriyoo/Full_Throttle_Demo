import json

class PeopleResponse():
    real_name= ''
    tz =''
    im =''
    activityPeriod=[]

    def toJSON(self):
        return {"real_name":self.real_name, "tz":self.tz, "id":self.im, "activity_periods":self.activityPeriod}


class ActivityResponse():
    start_time =""
    end_time =""

    def toJSON(self):
        return {"start_time":self.start_time, "end_time":self.end_time}



# class PeopleRequest():
#     real_name= ''
#     tz =''
#     im =''
#     activityPeriod=[]
#
#     def toJSON(self):
#         return {"real_name":self.real_name, "tz":self.tz, "id":self.im, "activity_periods":self.activityPeriod}
#
# class ActivityRequest():
#     im =''
#     start_time =""
#     end_time =""
#
#     def toJSON(self):
#         return {"start_time":self.start_time, "end_time":self.end_time}
