# from rest_framework import generics, serializers
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
# from rest_framework.validators import UniqueValidator
# from rest_framework.views import APIView
# from main.serializers import UserSerializer
# from rest_framework import permissions
# from rest_framework.permissions import IsAuthenticated,AllowAny
#
#
#
# # class UserSerializer1(serializers.ModelSerializer):
# #     name = serializers.CharField(max_length=30)
# #     surname = serializers.CharField(max_length=30)
# #     email = serializers.EmailField(
# #             required=True,
# #             validators=[UniqueValidator(queryset=User.objects.all())]
# #             )
# #     username = serializers.CharField(
# #             validators=[UniqueValidator(queryset=User.objects.all())]
# #             )
# #     password = serializers.CharField(min_length=8)
# #
# #     def create(self, validated_data):
# #         user = User.objects.create_user(validated_data['username'], name= validated_data['name'], email=validated_data['email'],
# #              password=validated_data['password'])
# #         return user
# #
# #     class Meta:
# #         model = User
# #         fields = '__all__'
# #         # fields = ('name', 'surname', 'username', 'email', 'password')
# #
# #         return user
#
# class UserCreate(generics.CreateAPIView):
#
#     def get_queryset(self):
#         return User.objects.all()
#
#     def get_serializer_class(self):
#         return UserSerializer
# #
# # class UserCreate(APIView):
# #
# #     def post(self, request):
# #         serializer = UserSerializer1(data=request.data)
# #         if serializer.is_valid():
# #             user = serializer.save()
# #             if user:
# #                 return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors)
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     http_method_names = ['get']
#     permission_classes = (IsAuthenticated,)
#
#
# @api_view(['POST'])
# def login(request):
#     serializer = AuthTokenSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data.get('user')
#     token, created = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key, 'username': user.username})
#
#
# @api_view(['POST'])
# def logout(request):
#     request.auth.delete()
#     return Response(status=status.HTTP_200_OK)
#
#
