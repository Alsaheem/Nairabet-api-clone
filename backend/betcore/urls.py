from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet,LeagueViewSet,TeamViewSet,BetViewSet

# defining the routers
router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet),
router.register(r'leagues', LeagueViewSet),
router.register(r'teams', TeamViewSet),
router.register(r'bets', BetViewSet),

# this is here incase i add some url patterns
urlpatterns = [
]

urlpatterns += router.urls