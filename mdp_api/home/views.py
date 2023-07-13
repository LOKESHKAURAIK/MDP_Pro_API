from django.shortcuts import render
# from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import (Services,Product,Dept_type,Offices,Industries,Career)
from .serializers import (services_serializers,product_serializers,Dept_type_serializers,contactus_serializers,
                          offices_serializers,industries_serializers,career_serializers,RegisterSerializer,LoginSerializer,)
from django.contrib.auth.models import User
from .models import Contact_us
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated #only for those who has authenticated
from rest_framework.authentication import TokenAuthentication #using token so here we have to import this

class ServicesView(APIView):
    def get(self, request):
        queryset = Services.objects.all()
        serializer = services_serializers(queryset, many = True)
        
        return Response({
                'status' : True,
                'message' : 'services fetched with GET',
                'data': serializer.data
            })

class ProductView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = product_serializers(queryset, many = True)
        
        return Response({
                'status' : True,
                'message' : 'products fetched with GET',
                'data': serializer.data
            })
        
class Dept_typeView(APIView):
    def get(self, request):
        queryset = Dept_type.objects.all()
        serializer = Dept_type_serializers(queryset, many = True)
        
        return Response({
                'status' : True,
                'message' : 'products fetched with GET',
                'data': serializer.data
            })
        
class OfficesView(APIView):
    def get(self, request):
        queryset = Offices.objects.all()
        serializer = offices_serializers(queryset, many = True)
        
        return Response({
                'status' : True,
                'message' : 'offices fetched with GET',
                'data': serializer.data
            })
        
# class ContactusView(APIView):

#     def post(self, request):
#         try: 
#             data = request.data
#             serializer = contactus_serializers(data = data)

#             if serializer.is_valid():
#                 user = User.objects.create(
#                     full_name = serializer.data['username'],
#                     phone_no = serializer.data['phone_no'],
#                     Email = serializer.data['Email'],
#                     subject = serializer.data['subject'],
#                     message = serializer.data['message']
                    
#                 )
#                 user.set_password(serializer.data['password'])
#                 user.save()

#                 return Response({
#                     'message' : 'account created',
#                     'status' : True,
#                     'data' : {}

#                 })

#             return Response({
#                 'status' : False,
#                 'message' : 'keys errors',
#                 'data' : serializer.errors
#             })

#         except Exception as e:
#             print(e)

class IndustriesView(APIView):
    def get(self, request):
        queryset = Industries.objects.all()
        serializer = industries_serializers(queryset, many = True)
        
        return Response({
                'status' : True,
                'message' : 'offices fetched with GET',
                'data': serializer.data
            })

class CareerView(APIView):
    def get(self, request):
        queryset = Career.objects.all()
        serializer = career_serializers(queryset, many = True)
        
        return Response({
                'status' : True,
                'message' : 'offices fetched with GET',
                'data': serializer.data
            })
        
class ContactCreateView(APIView):
     def post(self, request):
        try:
            data = request.data
            # data['animal_owner'] = request.user.id
            serializer = contactus_serializers(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message':'contacts created',
                    'data': serializer.data
                })
            return Response({
                    'status': False,
                    'message':'Invalid data',
                    'data': serializer.errors
                })

        except Exception as e:
            print(e)

            return Response({
                'status' : False,
                'message' : 'something went wrong',
                'data' : {}
            })
            

class RegisterAPI(APIView):

    def post(self, request):
        try: 
            data = request.data
            serializer = RegisterSerializer(data = data)

            if serializer.is_valid():
                user = User.objects.create(
                    username = serializer.data['username'],
                    email = serializer.data['email']
                )
                user.set_password(serializer.data['password'])
                user.save()

                return Response({
                    'message' : 'account created',
                    'status' : True,
                    'data' : {}

                })

            return Response({
                'status' : False,
                'message' : 'keys errors',
                'data' : serializer.errors
            })

        except Exception as e:
            print(e)
            
class LoginAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data = data)

            if serializer.is_valid():
                user ,_= authenticate(username = serializer.data['username'],password = serializer.data['password'])
                
                if user:
                    token=Token.objects.get_or_create(user=user)
                    return Response({
                        'message': 'login successful', 'status' : True,
                        'data' : {'token':str(token)}
                    })

                return Response({
                    'message' : 'invalid password',
                    'status' : False,
                    'data' : {}

                })

            return Response({
                'status' : False,
                'message' : 'keys errors',
                'data' : serializer.errors
            })

        except Exception as e:
            print(e)

            return Response({
                'status' : False,
                'message' : 'something went wrong',
                'data' : {}
            })