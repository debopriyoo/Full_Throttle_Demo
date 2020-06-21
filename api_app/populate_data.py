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
# from random import randint
#
# fakegen = Faker()
#
# def generate_im(size=9, chars=string.ascii_uppercase + string.digits):
#     ids= ''.join(random.choice(chars) for _ in range(size))
# #    ids.save()
#     return ids
# def generate_id():
#     ids= randint(0, 10)
#     return ids
#
# def populate(N=2):
#     print("Inside  populate")
#     for entry in range(N):
#         print("Populating user")
#         peoplerequest=People()
#         peoplerequest.id= generate_id()
#         peoplerequest.im = generate_im()
#         peoplerequest.real_name = fakegen.name()
#         peoplerequest.tz = fakegen.timezone()
#         activityRequest = ActivityPeriod()
#         activityRequest.start_time = fakegen.date_time_this_year()
#         activityRequest.end_time = fakegen.date_time_this_year()
#         activityRequest.im = peoplerequest
#         activityRequest.activityid = generate_id()
#
#
#         #People.objects.get_or_create(peoplerequest)[0]
#         try:
#             peoplerequest.save()
#             print("save passed")
#         except Exception as e:
#             print("save failed")
#             raise e
#
#
#
#         try:
#             activityRequest.save()
#             print("activity save passed")
#         except Exception as e:
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
