from django.urls import path, include
from rest_framework import routers
from .views import ProfileView,UserViewSet,ProfileDetailView

router = routers.SimpleRouter()
router.register(r'users', UserViewSet),

urlpatterns = [
    path('profiles/',ProfileView.as_view()),
    path('profile/<int:pk>',ProfileDetailView.as_view(),name='profile-detail'),
]
urlpatterns += router.urls
