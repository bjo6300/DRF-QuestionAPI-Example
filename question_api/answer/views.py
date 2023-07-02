from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import AnswerSerializer
from .models import Answer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    # def list(self, request):
    #     pass

    # def create(self, request): # POST
    #     pass

    # def retrieve(self, request, pk=None): # GET
    #     pass

    # def update(self, request, pk=None): # PUT
    #     pass

    # def partial_update(self, request, pk=None): # FETCH
    #     pass

    # def destroy(self, request, pk=None): # DELETE
    #     pass