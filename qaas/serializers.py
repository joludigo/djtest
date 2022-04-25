from django.contrib.auth.models import User, Group
from . import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class QuizzSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quizz
        fields = ["name"]


class QuestionSerializer(serializers.ModelSerializer):
    def validate_quizz(self, value):
        if self.context["request"].user != value.creator:
            raise serializers.ValidationError("Assigning Question to an invalid Quizz")
        return value

    class Meta:
        model = models.Question
        fields = ["quizz", "text"]


class AnswerSerializer(serializers.ModelSerializer):
    def validate_question(self, value):
        if self.context["request"].user != value.quizz.creator:
            raise serializers.ValidationError("Assigning Answer to an invalid Question")
        return value

    class Meta:
        model = models.Answer
        fields = ["question", "text", "correct"]


class QuizzInvitationSerializer(serializers.ModelSerializer):
    def validate_quizz(self, value):
        if self.context["request"].user != value.creator:
            raise serializers.ValidationError("Assigning Participants to an invalid Quizz")
        return value

    class Meta:
        model = models.QuizzInvitation
        fields = ["quizz", "email"]
