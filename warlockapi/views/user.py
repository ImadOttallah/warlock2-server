from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import User

class UserView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """GET all users"""
        users = User.objects.all()
        uid_query = request.query_params.get('uid', None)
        if uid_query is not None:
            users = users.filter(uid=uid_query)
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

    def create(self, request):
        """Handle PUT requests for a campaign"""
        user = User.objects.create(
            first_name = request.data["first_name"],
            last_name = request.data["last_name"],
            bio = request.data["bio"],
            profile_image_url = request.data["profile_image_url"],
            email = request.data["email"],
            created_on = request.data["created_on"],
            active = request.data["active"],
            uid = request.data["uid"]
      )
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a campaign"""
        user = User.objects.get(pk=pk)
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.bio = request.data["bio"]
        user.profile_image_url = request.data["profile_image_url"]
        user.email = request.data["email"]
        user.created_on = request.data["created_on"]
        user.active = request.data["active"]
        user.uid = request.data["uid"]
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle PUT requests for a campaign"""

        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'bio',
                  'profile_image_url',
                  'active',
                  'created_on',
                  'email',
                  'uid',
                  'id')
        depth = 1
