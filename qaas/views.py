from django.contrib.auth.models import User, Group
from .models import Quizz, Question, Answer, QuizzInvitation
from rest_framework import viewsets
from .permissions import IsCreator, IsParticipant
from qaas import serializers


class QuizzViewSet(viewsets.ModelViewSet):
    """API endpoint that Quizz to be viewed or edited."""

    queryset = Quizz.objects.all()
    serializer_class = serializers.QuizzSerializer
    permission_classes = [IsCreator]

    def get_queryset(self):
        return Quizz.objects.all().filter(creator=self.request.user).order_by("name")

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class QuestionViewSet(viewsets.ModelViewSet):
    """API endpoint that Quizz to be viewed or edited."""

    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [IsCreator]

    def get_queryset(self):
        return Question.objects.all().filter(quizz__creator=self.request.user).order_by("text")


class AnswerViewSet(viewsets.ModelViewSet):
    """API endpoint that Quizz to be viewed or edited."""

    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    permission_classes = [IsCreator]

    def get_queryset(self):
        return Answer.objects.all().filter(question__quizz__creator=self.request.user).order_by("text")


class QuizzInvitationViewSet(viewsets.ModelViewSet):
    """API endpoint that Quizz to be viewed or edited."""

    queryset = QuizzInvitation.objects.all()
    serializer_class = serializers.QuizzInvitationSerializer
    permission_classes = [IsCreator]
    http_method_names = ["get", "post", "head"]

    def get_queryset(self):
        return QuizzInvitation.objects.all().filter(quizz__creator=self.request.user).order_by("email")
