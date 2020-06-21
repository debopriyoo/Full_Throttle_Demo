# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','api_project.settings')
#
# import django
# django.setup()
#
# ##fake pop script
# import random
# from api_app.models import People,ActivityPeriod
# from faker import Faker
# import string
#
# fakegen = Faker()
#
#
# def generate_im(size=9, chars=string.ascii_uppercase + string.digits):
#     ids= ''.join(random.choice(chars) for _ in range(size))
# #    ids.save()
#     return ids
#
#
# def populate(N=2):
#     for entry in range(N):
#         fake_im = generate_im()
#         fake_real_name = fakegen.name()
#         fake_tz = fakegen.timezone()
#         fake_start_time = fakegen.date_time_this_year()
#         fake_end_time = fakegen.date_time_this_year()
#
#
#         peopletotal = People.objects.get_or_create(real_name=fake_real_name,
#                                                    tz=fake_tz,
#                                                    im=fake_im)[0]
#         print('peopletotal : ',peopletotal)
#
#         # activityperiodtotal = ActivityPeriod.objects.get_or_create(im=fake_im,start_time=fake_start_time,
#         #                                                            end_time=fake_end_time)[0]
#
# if __name__ == '__main__':
#     print('populating databases')
#     populate(2)
#     print('complete')
