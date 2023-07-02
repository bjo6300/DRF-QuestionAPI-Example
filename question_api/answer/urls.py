from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from answer.views import AnswerViewSet

router = routers.DefaultRouter()
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^',include(router.urls)),
]