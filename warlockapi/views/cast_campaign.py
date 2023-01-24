
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import CastCampaign,Cast,Campaign

class CastCampaignView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            cast_campaign = CastCampaign.objects.get(pk=pk)
            serializer = CastCampaignSerializer(cast_campaign)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET request for single campaign"""
        cast_campaigns = CastCampaign.objects.all()
        serializer = CastCampaignSerializer(cast_campaigns, many = True)
        return Response(serializer.data)

    def  create(self, request):
        """Handle GET request for single campaign"""
        cast = Cast.objects.get(pk=request.data["cast"])
        campaign = Campaign.objects.get(pk=request.data["campaign"])
        cast_campaign = CastCampaign.objects.create(
            cast = cast,
            campaign = campaign
        )
        serializer = CastCampaignSerializer(cast_campaign)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle GET request for single campaign"""
        cast = Cast.objects.get(pk=request.data["cast"])
        campaign = Campaign.objects.get(pk=request.data["campaign"])
        cast = Cast.objects.get(pk=pk)
        cast.cast = cast
        cast.campaign = campaign
        cast.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle GET request for single campaign"""
        cast_campaign = CastCampaign.objects.get(pk=pk)
        cast_campaign.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CastCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = CastCampaign
        fields = ('id', 'cast', 'campaign')
        depth = 1
