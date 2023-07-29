from rest_framework import serializers
from exelgen.models import XLModel


class DataSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = XLModel
        fields = ('data', 'name')
