from rest_framework import serializers 
from .models import Cookie

class CookieSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Cookie # tell django which model to use
        fields = ('id', 'type', 'cost', 'quantity',) # tell django which fields to include