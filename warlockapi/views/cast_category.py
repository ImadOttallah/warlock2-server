
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import CastCategory,CastType

class CastCategoryView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            cast_category = CastCategory.objects.get(pk=pk)
            serializer = CastCategorySerializer(cast_category)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET request for single campaign"""
        cast_categories = CastCategory.objects.all()
        serializer = CastCategorySerializer(cast_categories, many = True)
        return Response(serializer.data)

    def  create(self, request):
        """Handle GET request for single campaign"""
        cast_type = CastType.objects.get(pk=request.data["cast_type_id"])
        cast_category = CastCategory.objects.create(
            cast_type = cast_type
        )
        serializer = CastCategorySerializer(cast_category)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Handle GET request for single campaign"""
        cast_category = CastCategory.objects.get(pk=pk)
        cast_category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CastCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CastCategory
        fields = ('id', 'cast_type')
        depth = 2
