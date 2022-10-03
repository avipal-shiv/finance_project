
from rest_framework import serializers, viewsets, routers


from scrapes_data_app.models import *

class WebscrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webscrap
        fields = '__all__' 