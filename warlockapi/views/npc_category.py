
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import NpcCategory,Npc,NpcType

class NpcCategoryView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            npc_category = NpcCategory.objects.get(pk=pk)
            serializer = NpcCategorySerializer(npc_category)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET request for single campaign"""
        npc_categories = NpcCategory.objects.all()
        serializer = NpcCategorySerializer(npc_categories, many = True)
        return Response(serializer.data)

    def  create(self, request):
        """Handle GET request for single campaign"""
        npc = Npc.objects.get(pk=request.data["npc"])
        npc_type = NpcType.objects.get(pk=request.data["npc_type"])
        npc_category = NpcCategory.objects.create(
            npc = npc,
            npc_type = npc_type
        )
        serializer = NpcCategorySerializer(npc_category)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Handle GET request for single campaign"""
        npc_category = NpcCategory.objects.get(pk=pk)
        npc_category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class NpcCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = NpcCategory
        fields = ('id', 'npc', 'npc_type')
        depth = 2
