from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class services_serializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
        
class product_serializers(serializers.ModelSerializer):
    
    # def to_representation(self, instance):
    #     payload = {
    #         'hmis' : instance.hmis,
    #         'video_kyc' : instance.video_kyc,
    #         'voice_bot' : instance.voice_bot,
    #         'quality_control_work_monitoring_system' : instance.quality_control_work_monitoring_system,
    #         'gpc_based_attendance_monitoring_system' : instance.gpc_based_attendance_monitoring_system,
    #         'restaurant_portal' : instance.restaurant_portal,
    #         'finance_portal' : instance.finance_portal,
    #         'ravindra' : "Null"
            
    #     }
    #     return payload
    
    class Meta:
        model = Product
        fields = '__all__'
        
        
class Dept_type_serializers(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        payload = {
            'civil engineering' : instance.engg.civil_engineering,
            'mechanical_engineering' : instance.engg.mechanical_engineering,
            'electrical_engineering' : instance.engg.electrical_engineering,
            'department' : instance.department,
            'designation' : instance.designation,
            'job_location' : instance.job_location,
            'job_description' : instance.job_description,
            
            
        }
        return payload
    class Meta:
        model = Dept_type
        fields = '__all__'
        
class offices_serializers(serializers.ModelSerializer):
    class Meta:
        model = Offices
        fields = '__all__'
        
class contactus_serializers(serializers.ModelSerializer):
    
    class Meta:
        model = Contact_us
        fields = '__all__'


class industries_serializers(serializers.ModelSerializer):
    class Meta:
        model = Industries
        fields = '__all__'
        
class career_serializers(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'
        
        

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if 'username' in data:
            user = User.objects.filter(username = data['username'])
            if user.exists():
                raise serializers.ValidationError('username is already taken')

        if 'email' in data:
            user = User.objects.filter(email = data['email'])
            if user.exists():
                raise serializers.ValidationError('email is already taken')
        return data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if 'username' in data:
            user = User.objects.filter(username = data['username'])
            if not user.exists():
                raise serializers.ValidationError('username does not exist')
        return data

# def update(self, instance, data):
#     if 'animal_breed' in data:
#         animal_breed = data.pop('animal_breed')
#         instance.animal_breed.clear()
#         for ab in animal_breed:
#         # print(ab['animal_breed'])
#             animal_breed_obj = AnimalBreed.objects.get(animal_breed=ab['animal_breed'])
#             instance.animal_breed.add(animal_breed_obj)

#     if 'animal_color' in data:
#         animal_color = data.pop('animal_color')

#     instance.animal_name = data.get('animal_name', instance.animal_name)
#     instance.animal_description = data.get('animal_description', instance.animal_description)
#     instance.animal_gender = data.get('animal_gender', instance.animal_gender)

#     instance.save()

#     return instance

