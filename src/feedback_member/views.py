from rest_framework import viewsets
from .models import Feedback, Member
from .serializers import FeedbackSerializer, MemberSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(member=self.request.user)
