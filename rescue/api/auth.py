# from rest_framework import generics, status
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.authtoken.models import Token
# from api.models import CustomUser
# from api.serializers import CustomUserSerializer
#
#
# class UserCreateView(APIView):
#     permission_classes = (AllowAny,)
#
#     def post(self, request):
#         serializer = CustomUserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         user = CustomUser.objects.create(
#             email=serializer.validated_data['email'],
#             username=serializer.validated_data['email']
#         )
#
#         user.set_password(serializer.validated_data['password'])
#         user.save()
#
#         return Response(status=status.HTTP_201_CREATED)
#
#
# class UserView(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         if bool(request.user.is_anonymous):
#             return Response()
#
#         return Response(CustomUserSerializer(request.user).data)
#
#
# class UserList(generics.ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     permission_classes = (IsAuthenticated, )
#
#
# @api_view(['POST'])
# def login(request):
#     serializer = AuthTokenSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data.get('user')
#     token, created = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key})
#
#
# @api_view(['POST'])
# def logout(request):
#     request.auth.delete()
#     return Response(status=status.HTTP_200_OK)