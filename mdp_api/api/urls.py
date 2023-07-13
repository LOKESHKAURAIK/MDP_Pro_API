from home.views import *
from django.urls import path

urlpatterns = [
    path('services/', ServicesView.as_view()),
    path('product/', ProductView.as_view()),
    path('department/', Dept_typeView.as_view()),
    path('offices/', OfficesView.as_view()),
    path('contact/', ContactCreateView.as_view()),
    path('industries/', IndustriesView.as_view()),
    path('career/', CareerView.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    

]
