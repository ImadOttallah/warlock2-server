
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import NpcCategory,Npc,NpcType

class NpcCategoryView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            npccategory = NpcCategory.objects.get(pk=pk)
            serializer = NpcCategorySerializer(npccategory)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET request for single campaign"""
        npccategories = NpcCategory.objects.all()
        serializer = NpcCategorySerializer(npccategories, many = True)
        return Response(serializer.data)

    def  create(self, request):
        """Handle GET request for single campaign"""
        npc = Npc.objects.get(pk=request.data["npc"])
        npctype = NpcType.objects.get(pk=request.data["npc_type"])
        npccategory = NpcCategory.objects.create(
            npc = npc,
            npctype = npctype
        )
        serializer = NpcCategorySerializer(npccategory)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Handle GET request for single campaign"""
        npc_category = NpcCategory.objects.get(pk=pk)
        npc_category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class NpcCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = NpcCategory
        fields = ('id', 'npctype')
        depth = 2
