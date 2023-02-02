from django.http import HttpResponseServerError
from django.utils import timezone, dateformat
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import Campaign, User, Character, Cast, Npc


class CampaignView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            campaign = Campaign.objects.get(pk=pk)
            serializer = CampaignSerializer(campaign)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """GET all campaigns"""
        campaigns = Campaign.objects.all()
        character = request.query_params.get('character', None)
        npc = request.query_params.get('npc', None)
        cast = request.query_params.get('cast', None)
        if character is not None:
            characters = characters.filter(character_id=character)
            character = request.query_params.get('character_id', None)
        if npc is not None:
            npcs = npcs.filter(npc_id=npc)
            npc = request.query_params.get('npc_id', None)
        if cast is not None:
            casts = casts.filter(cast_id=cast)
            cast = request.query_params.get('cast_id', None)
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a campaign"""
        uid = request.data['user_id']
        user = User.objects.filter(uid=uid).first()
        campaign = Campaign.objects.create(
            name = request.data["name"],
            image = request.data["image"],
            # date_created = request.data["date_created"],
            description = request.data["description"],
            user=user,

        )
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a campaign"""

        campaign = Campaign.objects.get(pk=pk)
        campaign.name = request.data["name"]
        campaign.image = request.data["image"]
        # campaign.date_created = request.data["date_created"]
        campaign.date_created = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
        campaign.description = request.data["description"]
        character = Character.objects.get(pk=request.data["character"])
        campaign.character = character
        cast = Cast.objects.get(pk=request.data["cast"])
        campaign.cast = cast
        npc = Npc.objects.get(pk=request.data["npc"])
        campaign.npc = npc
        campaign.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle Delete requests for a campaign"""
        campaign = Campaign.objects.get(pk=pk)
        campaign.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'user', 'name', 'image', 'date_created', 'description', 'casts', 'npcs')
        depth = 2
    