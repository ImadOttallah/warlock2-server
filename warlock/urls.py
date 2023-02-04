"""warlock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from warlockapi.views import (
    CampaignView,
    CastCampaignView,
    CastCategoryView,
    CastTypeView,
    CastView,
    CharacterView,
    NpcCampaignView,
    NpcCategoryView,
    NpcTypeView,
    CharacterCampaignView,
    NpcView,
    UserView)
from warlockapi.views import register_user, check_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'campaigns', CampaignView, 'campaign')
router.register(r'cast_campaigns', CastCampaignView, 'cast_campaign')
router.register(r'cast_categories', CastCategoryView, 'cast_category')
router.register(r'npc_campaigns', NpcCampaignView, 'npc_campaign')
router.register(r'character_campaigns', CharacterCampaignView, 'character_campaign')
router.register(r'npc_categories', NpcCategoryView, 'npc_category')
router.register(r'characters', CharacterView, 'character')
router.register(r'cast_types', CastTypeView, 'cast_type')
router.register(r'npc_types', NpcTypeView, 'npc_type')
router.register(r'casts', CastView, 'cast')
router.register(r'npcs', NpcView, 'npc')
router.register(r'users', UserView, 'user')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
