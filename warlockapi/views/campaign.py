from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import Campaign, User


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
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a campaign"""
        user = User.objects.get(pk=request.data["user_id"])

        campaign = Campaign.objects.create(
            name = request.data["name"],
            image = request.data["image"],
            date_created = request.data["date_created"],
            description = request.data["description"],
            user=user

        )
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a campaign"""

        campaign = Campaign.objects.get(pk=pk)
        campaign.name = request.data["name"],
        campaign.image = request.data["image"],
        campaign.date_created = request.data["date_created"],
        campaign.description = request.data["description"],
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
        fields = ('id', 'user', 'name', 'image', 'date_created', 'description')
        depth = 1
    