from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import QuizzInvitation
from django.core.mail import send_mail

FAKE_EMAIL = "noreply@qaas.com"


@receiver(post_save, sender=QuizzInvitation)
def SendEmail(sender, instance, created, **kwargs):
    if created:
        # TODO
        # - check if email already assigned to an user
        #   exists --> send email with a link to the Quizz
        #   new email --> pre register user, send email
        subject = f"Join Quizz {instance.quizz.name}"
        message = "Invitation link..."
        from_email = FAKE_EMAIL
        to_email = instance.email
        # TODO Congure email: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
        # send_mail(subject, message, from_email, [to_email], fail_silently=False)
        print("Sending email...")
        print(f"{subject=} {message=} {from_email=} {to_email=}")
