from email.policy import default
from random import choices
from statistics import mode
from rest_framework import serializers
from RESTapp.models import Car, EXPIRY_CHOICES
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','model','make','color','description','license_date','license_expiry']
    # id = serializers.IntegerField(read_only=True)
    # model = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # make = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # color = serializers.CharField(required=True, allow_blank=False, max_length=20)
    # description = serializers.CharField(style={'base_template': 'textarea.html'})
    # license_date = serializers.DateField(required=True, allow_blank=False)
    # license_expiry = serializers.IntegerField(choices=EXPIRY_CHOICES, default=1)
    
    # def create(self, validated_data):
    #     return Car.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.model = validated_data.get('model', instance.model)
    #     instance.make = validated_data.get('make', instance.make)
    #     instance.color = validated_data.get('color', instance.color)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.license_date = validated_data.get('license_date', instance.license_date)
    #     instance.license_expiry = validated_data.get('license_expiry', instance.license_expiry)
    #     instance.save()
    #     return instance
