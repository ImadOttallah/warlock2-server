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
        castcategory = request.query_params.get('category', None)
        if castcategory is not None:
            categories = categories.filter(castcategory_id=castcategory)
        serializer = CastSerializer(casts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a campaign"""
        uid = request.data['user_id']
        user = User.objects.filter(uid=uid).first()
        castcategory = CastCategory.objects.get(pk=request.data["castcategory_id"])

        cast = Cast.objects.create(
            name = request.data["name"],
            stamina = request.data["stamina"],
            notes = request.data["notes"],
            user=user,
            castcategory=castcategory

        )
        # for id in request.data["castCategory"]:
        #     class_category_id = classes.objects.get(pk=id)
        #     charclass.objects.create(class_id=class_id, character_id=Character)
        serializer = CastSerializer(cast)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a campaign"""

        cast = Cast.objects.get(pk=pk)
        cast.name = request.data["name"]
        cast.stamina = request.data["stamina"]
        cast.notes = request.data["notes"]
        cast_category = CastCategory.objects.get(pk=request.data["castcategory_id"])
        cast.castcategory = cast_category
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
                  'name'
                  'stamina',
                  'notes',
                  'castcategory',
                  'user')
        depth = 2
    