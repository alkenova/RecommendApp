from django.contrib.auth.models import User
from auth_.serializers import MainUserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from .models import MainUser

class UserList(generics.ListCreateAPIView):
    queryset = MainUser.objects.all()
    serializer_class = MainUserSerializer
    permission_classes = (AllowAny)

    def get_queryset(self, request):
        queryset = self.get_queryset()
        serializer = MainUserSerializer(queryset, many=True)
        return Response(serializer.data)

    # def get_queryset(self, request):
    #     try:
    #         queryset = self.get_queryset()
    #         serializer = MainUserSerializer(queryset, many=True)
    #         return Response(serializer.data)
    #     catch