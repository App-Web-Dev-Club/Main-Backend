from rest_framework import serializers
from .models import *
from api.serializers import *


class PunchTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = KIDS_PunchTime
        fields = '__all__'

class ListPunchTimeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = KIDS_PunchTime
        fields = '__all__'

