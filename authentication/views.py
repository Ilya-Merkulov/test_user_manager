from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import LoginSerializer, RegistrationSerializer, UserSerializer
from .renderers import UserJSONRenderer
from django.views.decorators.csrf import csrf_exempt


from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse



@csrf_exempt
def user(request, id = 0):
    if request.method == 'GET':
        groups = User.objects.all()
        groups_serializer = UserSerializer(groups, many=True)
        return JsonResponse(groups_serializer.data, safe=False)

    elif request.method == 'PUT':
        groups_data = JSONParser().parse(request)
        group = User.objects.get(id=groups_data['id'])
        group_serializer = UserSerializer(group, data=groups_data)
        if group_serializer.is_valid():
            group_serializer.save()
            return JsonResponse('Group updating!!', safe=False)
        return JsonResponse('Failed to update Group!!!', safe=False)

    elif request.method == "DELETE":
        group = User.objects.get(id=id)
        group.delete()
        return JsonResponse('Delete!!', safe=False)

# class ListOfUsers(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     def get(self, request):
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many=True)
#         return Response({"users": users_serializer.data})


class RegistrationAPIView(APIView):
    """
    Registers a new user.   
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Creates a new User object.
        Username, email, and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'token': serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )

class LoginAPIView(APIView):
    """
    Logs in an existing user.
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Checks is user exists.
        Email and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = LoginSerializer

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put():
        serializer_data = request.data.get('user', {})

        # Паттерн сериализации, валидирования и сохранения - то, о чем говорили
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    #def delete 