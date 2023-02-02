from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import Character, User


class CharacterView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            character = Character.objects.get(pk=pk)
            serializer = CharacterSerializer(character)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """GET all campaigns"""
        characters = Character.objects.all()
        campaign = request.query_params.get('campaign', None)
        if campaign is not None:
            campaigns = campaigns.filter(campaign=campaign)
            
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a campaign"""
        # uid = request.data['user_id']
        # user = User.objects.filter(uid=uid).first()
        user = User.objects.get(pk=request.data["user_id"])

        character = Character.objects.create(
            name = request.data["name"],
            image = request.data["image"],
            traits = request.data["traits"],
            notes = request.data["notes"],
            spells = request.data["spells"],
            user=user

        )
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a campaign"""

        character = Character.objects.get(pk=pk)
        character.name = request.data["name"]
        character.image = request.data["image"]
        character.traits = request.data["traits"]
        character.notes = request.data["notes"]
        character.spells = request.data["spells"]
        character.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle Delete requests for a campaign"""
        character = Character.objects.get(pk=pk)
        character.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id',
                  'user',
                  'name',
                  'image',
                  'traits',
                  'notes',
                  'spells'
                  )
        depth = 2
    