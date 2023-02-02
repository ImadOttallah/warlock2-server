
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import CastCategory,CastType

class CastCategoryView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            castcategory = CastCategory.objects.get(pk=pk)
            serializer = CastCategorySerializer(castcategory)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET request for single campaign"""
        castcategories = CastCategory.objects.all()
        serializer = CastCategorySerializer(castcategories, many = True)
        return Response(serializer.data)

    def  create(self, request):
        """Handle GET request for single campaign"""
        casttype = CastType.objects.get(pk=request.data["cast_type_id"])
        castcategory = CastCategory.objects.create(
            casttype = casttype
        )
        serializer = CastCategorySerializer(castcategory)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Handle GET request for single campaign"""
        cast_category = CastCategory.objects.get(pk=pk)
        cast_category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CastCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CastCategory
        fields = ('id', 'casttype')
        depth = 2
