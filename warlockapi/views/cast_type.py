
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import CastType

class CastTypeView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            casttype = CastType.objects.get(pk=pk)
            serializer = CastTypeSerializer(casttype)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET request for single campaign"""
        casttypes = CastType.objects.all()
        serializer = CastTypeSerializer(casttypes, many = True)
        return Response(serializer.data)

    def  create(self, request):
        """Handle GET request for single campaign"""
        casttype = CastType.objects.create(
            name = request.data["name"]
        )
        serializer = CastTypeSerializer(casttype)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Handle GET request for single campaign"""
        cast_type = CastType.objects.get(pk=pk)
        cast_type.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CastTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CastType
        fields = ('id', 'name')
        depth = 2
