from django.shortcuts import render
from api.serializers import member_Serializer
from api.models import Member
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly as d
#from rest_framework.authentication import TokenAuthentication

#from api.permission import IsReadOnly,isGetALL,isname

from rest_framework_simplejwt.authentication import JWTAuthentication
class member_view(ModelViewSet):
    queryset=Member.objects.all()
    serializer_class=member_Serializer
    authentication_classes = [JWTAuthentication] 
    permission_classes=[IsAuthenticated]