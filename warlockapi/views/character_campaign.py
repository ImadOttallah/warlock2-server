
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import Campaign, Character, CharacterCampaign

class CharacterCampaignView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            charactercampaign = CharacterCampaign.objects.get(pk=pk)
            serializer = CharacterCampaignSerializer(charactercampaign)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET request for single campaign"""
        charactercampaigns = CharacterCampaign.objects.all()
        serializer = CharacterCampaignSerializer(charactercampaigns, many = True)
        return Response(serializer.data)

    def  create(self, request):
        """Handle GET request for single campaign"""
        character = Character.objects.get(pk=request.data["character"])
        campaign = Campaign.objects.get(pk=request.data["campaign"])
        charactercampaign = CharacterCampaign.objects.create(
            character = character,
            campaign = campaign
        )
        serializer = CharacterCampaignSerializer(charactercampaign)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle GET request for single campaign"""
        character = Character.objects.get(pk=request.data["character"])
        campaign = Campaign.objects.get(pk=request.data["campaign"])
        character = Character.objects.get(pk=pk)
        character.character = character
        character.campaign = campaign
        character.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle GET request for single campaign"""
        character_campaign = CharacterCampaign.objects.get(pk=pk)
        character_campaign.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CharacterCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterCampaign
        fields = ('id', 'character', 'campaign')
        depth = 2
