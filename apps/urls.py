from django.urls import path
from apps.views import *

urlpatterns = [
    path('', home, name='index'),
    path('contact/', contact, name='contact'),
    path('index/', home, name='index'),
    path('topics_listing/', topics_listing, name='topics-listing'),
    path('topics_detail/', topics_detail, name='topics-detail'),
    ]
