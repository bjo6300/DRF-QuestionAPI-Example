from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers

from question.views import QuestionViewSet


router = routers.DefaultRouter() 
router.register('question', QuestionViewSet) 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(router.urls)),
]