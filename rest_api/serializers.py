from rest_framework.serializers import ModelSerializer
from base.models import Register

class NewsModelSerializer(ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'