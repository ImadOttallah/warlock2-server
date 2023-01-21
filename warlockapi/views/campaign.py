from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import Campaign


class CampaignView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        campaign = Campaign.objects.get(pk=pk)
        serializer = CampaignsSerializer(campaign)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        campaign = Campaign.objects.all()
        serializer = CampaignsSerializer(campaign, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle GET operations"""
        campaign = Campaign.objects.create(
            label=request.data["label"]
        )
        serializer = CampaignsSerializer(campaign)
        return Response(serializer.data)

    def destroy(self, request, pk):
        campaign = Campaign.objects.get(pk=pk)
        campaign.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'user', 'name', 'image', 'date_created', 'description')
        depth = 1
    