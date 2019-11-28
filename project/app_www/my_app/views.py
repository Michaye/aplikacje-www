from my_app.models import Room, Comment
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from my_app.serializers import RoomSerializer, CommentSerializer


class Index(APIView):
    def get(self, request):
        return Response(status=200)


class Users(APIView):
    def get(self, request):
        return Response(status=200)

    parser_classes = [JSONParser]

    def post(self, request):
        return Response({"data": "success"}, 200)


class Rooms(APIView):
    def get(self, request):
        return Response({"rooms": RoomSerializer(Room.objects.all(), many=True).data}, status=200)


class Comments(APIView):
    def get(self, request):
        return Response({"comments": CommentSerializer(Comment.objects.all(), many=True).data}, status=200)
