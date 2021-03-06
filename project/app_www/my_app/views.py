from my_app.models import Room, Comment, CustomUser
from my_app.serializers import RoomSerializer, CommentSerializer, CustomUserSerializer, AddressSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView


class Index(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
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

    def get(self, request):
        return Response({"address": AddressSerializer(self.request.user.address).data}, status=200)

    def post(self, request):
        if not self.request.user.address:
            serializer = AddressSerializer(data=self.request.data)
        else:
            serializer = AddressSerializer(self.request.user.address, data=self.request.data, partial=True)

        if serializer.is_valid():
            address = serializer.save()
            self.request.user.address = address
            self.request.user.save()
            return Response({"message": "Address changed!"}, 200)
        else:
            return Response({"message": "Address creation failed!"}, 400)


class BanUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, id):
        user = CustomUser.objects.get(id=id)
        user.is_active = False
        user.save()
        return Response({"message": f"User {user} banned!"}, 200)


class FollowUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self, request):
        return Response({"message": "Send User login in post to follow"}, 200)

    def post(self, request):
        if "login" in self.request.data:
            try:
                self.request.user.followed.add(CustomUser.objects.get(login=self.request.data["login"]))
            except:
                return Response({"message": "User does not exist"}, 400)
        else:
            return Response({"message": "Error: send User login in post to follow"}, 400)

        return Response({"message": "User followed!"}, 200)
