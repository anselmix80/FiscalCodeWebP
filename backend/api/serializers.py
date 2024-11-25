# Serializers define the API representation.
from rest_framework import serializers
from .models import Common
import platform

# Define the serializers
# Serialize the input data
class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    date = serializers.DateField()
    city = serializers.CharField(max_length=100)
    sex = serializers.CharField(max_length=1)

# Serialize the output data
# Serialize the commons data
class CommonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Common
        fields = "__all__"

# Serialize the server name
# Retrieve the server name
class ServerSerializer(serializers.Serializer):
    server = platform.node()