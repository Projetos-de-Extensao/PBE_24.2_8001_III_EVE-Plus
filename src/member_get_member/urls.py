from rest_framework.routers import DefaultRouter
from .views import ConviteViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'getmember', ConviteViewSet)
router.register(r'feedback', FeedbackViewSet)
urlpatterns = router.urls