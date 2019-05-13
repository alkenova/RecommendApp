from rest_framework import serializers
from auth_.models import MainUser, UserManager

class MainUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    full_name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)

    class Meta:
        model = MainUser
        fields = ('id', 'username', 'email', 'full_name',
                  'phone', 'is_active', 'is_staff', 'is_admin', )