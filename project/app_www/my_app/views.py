from my_app.models import Room, Comment, CustomUser
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from my_app.serializers import RoomSerializer, CommentSerializer, CustomUserSerializer


class Index(APIView):
    def get(self, request):
        return Response(status=200)


class Users(APIView):
    def get(self, request):
        return Response(
            {"Users": CustomUserSerializer(CustomUser.objects.all(), many=True).data},
            status=200,
        )


class Rooms(APIView):
    def get(self, request):
        return Response(
            {"rooms": RoomSerializer(Room.objects.all(), many=True).data}, status=200
        )


class Comments(APIView):
    def get(self, request):
        return Response(
            {"comments": CommentSerializer(Comment.objects.all(), many=True).data},
            status=200,
        )


class CreateUser(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = CustomUserSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created!"}, 200)
        else:
            return Response({"message": "User creation failed!"}, 400)
