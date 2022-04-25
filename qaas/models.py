from django.db import models
from django.conf import settings


class Quizz(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={"groups__name": "creator"}, on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "creator"], name="Quizz_UNIQUE"),
        ]


class Question(models.Model):
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    text = models.CharField(max_length=512)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["quizz", "text"], name="Question_UNIQUE"),
        ]


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    correct = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["question", "text"], name="Answer_UNIQUE"),
        ]


class QuizzInvitation(models.Model):
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    email = models.CharField(max_length=512)
    accepted = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["quizz", "email"], name="QuizzInvitation_UNIQUE"),
        ]


class QuizzParticipant(models.Model):
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    participant = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={"groups__name": "participant"}, on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["quizz", "participant"], name="QuizzParticipant_UNIQUE"),
        ]


class ParticipantAnswer(models.Model):
    participant = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={"groups__name": "participant"}, on_delete=models.CASCADE
    )
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["participant", "answer"], name="ParticipantAnswer_UNIQUE"),
        ]
