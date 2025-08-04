from rest_framework.serializers import ModelSerializer
from api.models import Member
class member_Serializer(ModelSerializer):
    class Meta:

        model=Member
        fields=('__all__')