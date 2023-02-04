from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import Npc, User, NpcCategory

class NpcView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            npc = Npc.objects.get(pk=pk)
            serializer = NpcSerializer(npc)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """GET all campaigns"""
        npcs = Npc.objects.all()
        npccategory = request.query_params.get('category', None)
        if npccategory is not None:
            categories = categories.filter(npccategory_id=npccategory)
        serializer = NpcSerializer(npcs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a campaign"""
        uid = request.data['user_id']
        user = User.objects.filter(uid=uid).first()
        npccategory = NpcCategory.objects.get(pk=request.data["npccategory"])

        npc = Npc.objects.create(
            name = request.data["name"],
            stamina = request.data["stamina"],
            notes = request.data["notes"],
            user=user,
            npccategory=npccategory
        )
        serializer = NpcSerializer(npc)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a campaign"""

        npc = Npc.objects.get(pk=pk)
        npc.name = request.data["name"]
        npc.stamina = request.data["stamina"]
        npc.notes = request.data["notes"]
        npccategory = NpcCategory.objects.get(pk=request.data["npccategory"])
        npc.npccategory = npccategory
        npc.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle Delete requests for a campaign"""
        npc = Npc.objects.get(pk=pk)
        npc.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class NpcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Npc
        fields = ('id',
                  'user',
                  'name',
                  'stamina',
                  'notes',
                  'npccategory')
        depth = 2
    