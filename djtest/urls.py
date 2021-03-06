from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from qaas import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r"quizzess", views.QuizzViewSet)
router.register(r"questions", views.QuestionViewSet)
router.register(r"answers", views.AnswerViewSet)
router.register(r"quizz_invitations", views.QuizzInvitationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
]
