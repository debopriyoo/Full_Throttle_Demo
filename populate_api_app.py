# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','api_project.settings')
#
# import django
# django.setup()
#
# from api_app.People import *
# ##fake pop script
# import random
# from api_app.models import People,ActivityPeriod
# from faker import Faker
# import string
#
# fakegen = Faker()
#
# def generate_im():
#     ids= random.random()
#     return ids
#
#
# def populate(N=2):
#     print("Inside  populate")
#     for entry in range(N):
#         print("Populating user")
#         peoplerequest=PeopleRequest()
#         peoplerequest.im = generate_im()
#         peoplerequest.real_name = fakegen.name()
#         peoplerequest.tz = fakegen.timezone()
#         activityRequest = ActivityRequest()
#         activityRequest.start_time = fakegen.date_time_this_year()
#         activityRequest.end_time = fakegen.date_time_this_year()
#         activityRequest.im = peoplerequest.im
#         activityRequest.activityid = generate_im()
#
#
#         #People.objects.get_or_create(peoplerequest)[0]
#         try:
#             peoplerequest.save()
#             print("save passed")
#         except Exception e:
#             print("save failed")
#             raise e
#
#
#
#         try:
#             activityRequest.save()
#             print("activity save passed")
#         except Exception e:
#             print("activity save failed")
#             raise e
#
#
#
#         #activityperiodtotal = ActivityPeriod.objects.get_or_create(activityRequest)[0]
#         #print("activityperiodtotal:",activityperiodtotal)
#
# if __name__ == '__main__':
#     print('populating databases')
#     populate(2)
#     print('complete')
