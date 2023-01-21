from django.db import models
from .user import User

class Character(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    community = models.CharField(max_length=50)
    background = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    stamina = models.CharField(max_length=50)
    luck = models.CharField(max_length=50)
    pluck = models.CharField(max_length=50)
    appraise_skill = models.CharField(max_length=50)
    athletics_skill = models.CharField(max_length=50)
    bargain_skill = models.CharField(max_length=50)
    blunt_skill = models.CharField(max_length=50)
    bow_skill = models.CharField(max_length=50)
    bow_skill = models.CharField(max_length=50)
    brawling_skill = models.CharField(max_length=50)
    command_skill = models.CharField(max_length=50)
    crossbow_skill = models.CharField(max_length=50)
    diplomacy_skill = models.CharField(max_length=50)
    disguise_skill = models.CharField(max_length=50)
    dodge_skill = models.CharField(max_length=50)
    endurance_skill = models.CharField(max_length=50)
    history_skill = models.CharField(max_length=50)
    incantation_skill = models.CharField(max_length=50)
    intimidate_skill = models.CharField(max_length=50)
    language_skill = models.CharField(max_length=50)
    large_blade_skill = models.CharField(max_length=50)
    lie_skill = models.CharField(max_length=50)
    medicine_skill = models.CharField(max_length=50)
    navigation_skill = models.CharField(max_length=50)
    ostler_skill = models.CharField(max_length=50)
    persuasion_skill = models.CharField(max_length=50)
    pole_arm_skill = models.CharField(max_length=50)
    repair_skill = models.CharField(max_length=50)
    sleight_of_hand_skill = models.CharField(max_length=50)
    small_blade_skill = models.CharField(max_length=50)
    spot_skill = models.CharField(max_length=50)
    stealth_skill = models.CharField(max_length=50)
    streetwise_skill = models.CharField(max_length=50)
    survival_skill = models.CharField(max_length=50)
    swimming_skill = models.CharField(max_length=50)
    thrown_skill = models.CharField(max_length=50)
    possesions = models.CharField(max_length=50)
    weapons = models.CharField(max_length=50)
    traits = models.CharField(max_length=200)
    notes = models.CharField(max_length=300)
    spells = models.CharField(max_length=300)
