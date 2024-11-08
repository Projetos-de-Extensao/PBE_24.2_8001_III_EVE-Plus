from rest_framework.routers import DefaultRouter
from .views import ConviteViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'member_get', ConviteViewSet)
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = router.urls