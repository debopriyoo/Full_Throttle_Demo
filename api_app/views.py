from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from api_app.models import *
import json
from django.core import serializers
from api_app.People import *
# from api_app.populate_data import *


# Create your views here.

class PersonView(APIView):

    def get(self, request, format=None):
        try:
            data=json.loads(serializers.serialize("json", People.objects.all()))
            print(data)
            # print(data[0]["fields"]["real_name"])
            responselist=[]

            for obj in data:
                peopleResponse = PeopleResponse()
                print(peopleResponse)
                peopleResponse.real_name = obj["fields"]["real_name"]
                peopleResponse.tz = obj["fields"]["tz"]
                peopleResponse.im = obj["fields"]["im"]
                response=[]
                peopleResponse.activityPeriod=[]
                #response = ActivityPeriod.objects.filter(im=peopleResponse.im)
                print('peopleResponse.im :',peopleResponse.im)
                response = json.loads(serializers.serialize("json", ActivityPeriod.objects.filter(im = peopleResponse.im)))
                print('Response:',response)

                for res in response:
                    activityResponse = ActivityResponse()
                    activityResponse.start_time = res["fields"]['start_time']
                    activityResponse.end_time = res["fields"]["end_time"]
                    print('activityResponse:',activityResponse)
                    peopleResponse.activityPeriod.append(activityResponse.toJSON())
                    print('peopleResponse.activityPeriod:',peopleResponse.activityPeriod)
                print('peopleResponse:',peopleResponse)
                responselist.append(peopleResponse.toJSON())
                print('responselist :',responselist)
            return Response({"ok": True,"members":responselist},status=status.HTTP_200_OK)

        except:

            return Response({"ok":False,"members":None},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    # def post(self, request):
    #     print("Post call to PeopleView")
    #     populate()
    #     print("Post call to PeopleView Completed")
    #     return Response({},status=status.HTTP_200_OK)
