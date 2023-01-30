from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import Cast, User, CastCategory


class CastView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            cast = Cast.objects.get(pk=pk)
            serializer = CastSerializer(cast)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """GET all campaigns"""
        casts = Cast.objects.all()
        cast_category = request.query_params.get('category', None)
        if cast_category is not None:
            categories = categories.filter(cast_category_id=cast_category)
        serializer = CastSerializer(casts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a campaign"""
        user = User.objects.get(pk=request.data["user_id"])
        cast_category = CastCategory.objects.get(pk=request.data["cast_category"])

        cast = Cast.objects.create(
            name = request.data["name"],
            description = request.data["description"],
            image = request.data["image"],
            actions = request.data["actions"],
            weapon = request.data["weapon"],
            armour = request.data["armour"],
            adventuring_skills = request.data["adventuring_skills"],
            stamina = request.data["stamina"],
            notes = request.data["notes"],
            user=user,
            cast_category=cast_category

        )
        serializer = CastSerializer(cast)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a campaign"""

        cast = Cast.objects.get(pk=pk)
        cast.name = request.data["name"]
        cast.description = request.data["description"]
        cast.image = request.data["image"]
        cast.actions = request.data["actions"]
        cast.weapon = request.data["weapon"]
        cast.armour = request.data["armour"]
        cast.adventuring_skills = request.data["adventuring_skills"]
        cast.stamina = request.data["stamina"]
        cast.notes = request.data["notes"]
        cast_category = CastCategory.objects.get(pk=request.data["cast_category"])
        cast.cast_category = cast_category
        cast.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle Delete requests for a campaign"""
        cast = Cast.objects.get(pk=pk)
        cast.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
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
                  'notes',
                  'cast_category')
        depth = 2
    