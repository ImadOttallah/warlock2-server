from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import Npc, User


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
        serializer = NpcSerializer(npcs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a campaign"""
        user = User.objects.get(pk=request.data["user_id"])

        npc = Npc.objects.create(
            name = request.data["name"],
            description = request.data["description"],
            image = request.data["image"],
            actions = request.data["actions"],
            weapon = request.data["weapon"],
            armour = request.data["armour"],
            adventuring_skills = request.data["adventuring_skills"],
            stamina = request.data["stamina"],
            notes = request.data["notes"],
            user=user

        )
        serializer = NpcSerializer(npc)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a campaign"""

        npc = Npc.objects.get(pk=pk)
        npc.name = request.data["name"]
        npc.description = request.data["description"]
        npc.image = request.data["image"]
        npc.actions = request.data["actions"]
        npc.weapon = request.data["weapon"]
        npc.armour = request.data["armour"]
        npc.adventuring_skills = request.data["adventuring_skills"]
        npc.stamina = request.data["stamina"]
        npc.notes = request.data["notes"]
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
                  'description',
                  'image',
                  'actions',
                  'weapon',
                  'armour',
                  'adventuring_skills',
                  'stamina',
                  'notes')
        depth = 2
    