from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from warlockapi.models import Character, User, Campaign


class CharacterView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single campaign"""
        try:
            character = Character.objects.get(pk=pk)
            serializer = CharacterSerializer(character)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """GET all campaigns"""
        characters = Character.objects.all()
        campaign = request.query_params.get('campaign', None)
        if campaign is not None:
            campaigns = campaigns.filter(campaign=campaign)
            
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a campaign"""
        user = User.objects.get(pk=request.data["user_id"])
        campaign = Campaign.objects.get(pk=request.data["campaign"])

        character = Character.objects.create(
            name = request.data["name"],
            image = request.data["image"],
            community = request.data["community"],
            background = request.data["background"],
            career = request.data["career"],
            stamina = request.data["stamina"],
            luck = request.data["luck"],
            pluck = request.data["pluck"],
            appraise_skill = request.data["appraise_skill"],
            athletics_skill = request.data["athletics_skill"],
            bargain_skill = request.data["bargain_skill"],
            blunt_skill = request.data["blunt_skill"],
            bow_skill = request.data["bow_skill"],
            brawling_skill = request.data["brawling_skill"],
            command_skill = request.data["command_skill"],
            crossbow_skill = request.data["crossbow_skill"],
            diplomacy_skill = request.data["diplomacy_skill"],
            disguise_skill = request.data["disguise_skill"],
            dodge_skill = request.data["dodge_skill"],
            endurance_skill = request.data["endurance_skill"],
            history_skill = request.data["history_skill"],
            incantation_skill = request.data["incantation_skill"],
            intimidate_skill = request.data["intimidate_skill"],
            language_skill = request.data["language_skill"],
            large_blade_skill = request.data["large_blade_skill"],
            lie_skill = request.data["lie_skill"],
            medicine_skill = request.data["medicine_skill"],
            navigation_skill = request.data["navigation_skill"],
            ostler_skill = request.data["ostler_skill"],
            persuasion_skill = request.data["persuasion_skill"],
            pole_arm_skill = request.data["pole_arm_skill"],
            repair_skill = request.data["repair_skill"],
            sleight_of_hand_skill = request.data["sleight_of_hand_skill"],
            small_blade_skill = request.data["small_blade_skill"],
            spot_skill = request.data["spot_skill"],
            stealth_skill = request.data["stealth_skill"],
            streetwise_skill = request.data["streetwise_skill"],
            survival_skill = request.data["survival_skill"],
            swimming_skill = request.data["swimming_skill"],
            thrown_skill = request.data["thrown_skill"],
            possesions = request.data["possesions"],
            weapons = request.data["weapons"],
            traits = request.data["traits"],
            notes = request.data["notes"],
            spells = request.data["spells"],
            campaign = campaign,
            user=user

        )
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a campaign"""

        character = Character.objects.get(pk=pk)
        character.name = request.data["name"]
        character.image = request.data["image"]
        character.community = request.data["community"]
        character.background = request.data["background"]
        character.career = request.data["career"]
        character.stamina = request.data["stamina"]
        character.luck = request.data["luck"]
        character.pluck = request.data["pluck"]
        character.appraise_skill = request.data["appraise_skill"]
        character.athletics_skill = request.data["athletics_skill"]
        character.bargain_skill = request.data["bargain_skill"]
        character.blunt_skill = request.data["blunt_skill"]
        character.bow_skill = request.data["bow_skill"]
        character.brawling_skill = request.data["brawling_skill"]
        character.command_skill = request.data["command_skill"]
        character.crossbow_skill = request.data["crossbow_skill"]
        character.diplomacy_skill = request.data["diplomacy_skill"]
        character.disguise_skill = request.data["disguise_skill"]
        character.dodge_skill = request.data["dodge_skill"]
        character.endurance_skill = request.data["endurance_skill"]
        character.history_skill = request.data["history_skill"]
        character.incantation_skill = request.data["incantation_skill"]
        character.intimidate_skill = request.data["intimidate_skill"]
        character.language_skill = request.data["language_skill"]
        character.large_blade_skill = request.data["large_blade_skill"]
        character.lie_skill = request.data["lie_skill"]
        character.medicine_skill = request.data["medicine_skill"]
        character.navigation_skill = request.data["navigation_skill"]
        character.ostler_skill = request.data["ostler_skill"]
        character.persuasion_skill = request.data["persuasion_skill"]
        character.pole_arm_skill = request.data["pole_arm_skill"]
        character.repair_skill = request.data["repair_skill"]
        character.sleight_of_hand_skill = request.data["sleight_of_hand_skill"]
        character.small_blade_skill = request.data["small_blade_skill"]
        character.spot_skill = request.data["spot_skill"]
        character.stealth_skill = request.data["stealth_skill"]
        character.streetwise_skill = request.data["streetwise_skill"]
        character.survival_skill = request.data["survival_skill"]
        character.swimming_skill = request.data["swimming_skill"]
        character.thrown_skill = request.data["thrown_skill"]
        character.possesions = request.data["possesions"]
        character.weapons = request.data["weapons"]
        character.traits = request.data["traits"]
        character.notes = request.data["notes"]
        character.spells = request.data["spells"]
        campaign = Campaign.objects.get(pk=request.data["campaign"])
        campaign = campaign,
        character.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle Delete requests for a campaign"""
        character = Character.objects.get(pk=pk)
        character.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id',
                  'user',
                  'name',
                  'image',
                  'community',
                  'background',
                  'career',
                  'stamina',
                  'luck',
                  'pluck',
                  'appraise_skill',
                  'athletics_skill',
                  'bargain_skill',
                  'blunt_skill',
                  'bow_skill',
                  'brawling_skill',
                  'command_skill',
                  'crossbow_skill',
                  'diplomacy_skill',
                  'disguise_skill',
                  'dodge_skill',
                  'endurance_skill',
                  'history_skill',
                  'incantation_skill',
                  'intimidate_skill',
                  'language_skill',
                  'large_blade_skill',
                  'lie_skill',
                  'medicine_skill',
                  'navigation_skill',
                  'ostler_skill',
                  'persuasion_skill',
                  'pole_arm_skill',
                  'repair_skill',
                  'sleight_of_hand_skill',
                  'small_blade_skill',
                  'spot_skill',
                  'stealth_skill',
                  'streetwise_skill',
                  'survival_skill',
                  'swimming_skill',
                  'thrown_skill',
                  'possesions',
                  'weapons',
                  'traits',
                  'notes',
                  'spells',
                  'campaign')
        depth = 2
    