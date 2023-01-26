
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import NpcType

class NpcTypeView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            npc_type = NpcType.objects.get(pk=pk)
            serializer = NpcTypeSerializer(npc_type)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET request for single campaign"""
        npc_types = NpcType.objects.all()
        serializer = NpcTypeSerializer(npc_types, many = True)
        return Response(serializer.data)

    def  create(self, request):
        """Handle GET request for single campaign"""
        npc_type = NpcType.objects.create(
            name = request.data["name"]
        )
        serializer = NpcTypeSerializer(npc_type)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Handle GET request for single campaign"""
        npc_type = NpcType.objects.get(pk=pk)
        npc_type.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class NpcTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = NpcType
        fields = ('id', 'name')
        depth = 2
