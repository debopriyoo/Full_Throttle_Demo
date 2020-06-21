from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_app import views


# router = DefaultRouter()
# router.register('hello-viewset', views.HelloViewSet,basename='hello-viewset')

urlpatterns = [
    path('user/', views.PersonView.as_view()),
    #path('api/', include('profiles_api.urls')),
    #
]
