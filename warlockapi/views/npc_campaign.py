
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import NpcCampaign,Npc,Campaign

class NpcCampaignView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            npc_campaign = NpcCampaign.objects.get(pk=pk)
            serializer = NpcCampaignSerializer(npc_campaign)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET request for single campaign"""
        npc_campaigns = NpcCampaign.objects.all()
        serializer = NpcCampaignSerializer(npc_campaigns, many = True)
        return Response(serializer.data)

    def  create(self, request):
        """Handle GET request for single campaign"""
        npc = Npc.objects.get(pk=request.data["npc"])
        campaign = Campaign.objects.get(pk=request.data["campaign"])
        npc_campaign = NpcCampaign.objects.create(
            npc = npc,
            campaign = campaign
        )
        serializer = NpcCampaignSerializer(npc_campaign)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle GET request for single campaign"""
        npc = Npc.objects.get(pk=request.data["npc"])
        campaign = Campaign.objects.get(pk=request.data["campaign"])
        npc = Npc.objects.get(pk=pk)
        npc.npc = npc
        npc.campaign = campaign
        npc.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle GET request for single campaign"""
        npc_campaign = NpcCampaign.objects.get(pk=pk)
        npc_campaign.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class NpcCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = NpcCampaign
        fields = ('id', 'npc', 'campaign')
        depth = 2
