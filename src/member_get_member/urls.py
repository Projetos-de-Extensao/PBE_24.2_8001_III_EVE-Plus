from rest_framework.routers import DefaultRouter
from .views import ConviteViewSet

router = DefaultRouter()
router.register(r'member_get', ConviteViewSet)

urlpatterns = router.urls