from my_app.models import Room, Comment, CustomUser
from my_app.serializers import RoomSerializer, CommentSerializer, CustomUserSerializer, AddressSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class Index(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = CustomUser.objects.get(login="testtest")
        user.followed.add(CustomUser.objects.get(login="epeloo"))
        return Response({"message": f"Hello {self.request.user}!"}, status=200)


class Users(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {"Users": CustomUserSerializer(CustomUser.objects.all(), many=True).data},
            status=200,
        )


class Rooms(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {"rooms": RoomSerializer(Room.objects.all(), many=True).data}, status=200
        )


class Comments(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {"comments": CommentSerializer(Comment.objects.all(), many=True).data},
            status=200,
        )


class CreateUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = CustomUserSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created!"}, 200)
        else:
            return Response({"message": "User creation failed!"}, 400)


class CreateRoom(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = RoomSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Room created!"}, 200)
        else:
            return Response({"message": "Cannot create new room!"}, 400)


class AddComment(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = CommentSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Added new comment!"}, 200)
        else:
            return Response(
                {"message": "Cannot add comment!", "errors": serializer.errors}, 400
            )


class EditProfile(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def patch(self, request):
        serializer = CustomUserSerializer(
            self.request.user, data=self.request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated!"}, 200)
        else:
            return Response({"error": serializer.errors}, 400)


class EditRoom(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def patch(self, request):
        try:
            room = Room.objects.get(name=self.request.data["current_name"])
        except Exception:
            return Response({"error": "Room does not exists!"}, 400)

        serializer = RoomSerializer(room, data=self.request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Room updated!"}, 200)
        else:
            return Response({"error": serializer.errors}, 400)


class CreateUserAddress(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self, request, id):
        user = CustomUser.objects.get(id=id)
        return Response({"address": AddressSerializer(user.address).data}, status=200)

    def post(self, request, id):
        user = CustomUser.objects.get(id=id)
        if not user.address:
            serializer = AddressSerializer(data=self.request.data)
        else:
            serializer = AddressSerializer(user.address, data=self.request.data, partial=True)

        if serializer.is_valid():
            address = serializer.save()
            user.address = address
            user.save()
            return Response({"message": "Address changed!"}, 200)
        else:
            return Response({"message": "Address creation failed!"}, 400)
