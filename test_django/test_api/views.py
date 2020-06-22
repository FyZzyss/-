from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser

from .models import Polls, UserAnswer
from test_api.serializers import PollsSerializer, UserAnswerSerializer
from datetime import datetime, timedelta

import uuid


class PollsList(generics.ListAPIView):
    queryset = Polls.objects.exclude(finish_date__lte=(datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d'))
    model = Polls
    serializer_class = PollsSerializer

    def get(self, request, *args, **kwargs):
        if request.session.get('uuid', None):
            pass
        else:
            request.session['uuid'] = str(uuid.uuid1()).replace('-', '')
        return super().get(self, request, *args, **kwargs)


class SinglePollsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Polls.objects.all()
    serializer_class = PollsSerializer


class PollsCreate(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Polls.objects.all()
    model = Polls
    serializer_class = PollsSerializer


class PollsAnswer(generics.ListCreateAPIView):
    model = UserAnswer
    serializer_class = UserAnswerSerializer

    '''def get_serializer_context(self):
        context = super().get_serializer_context()
        print(self.request.session['uuid'])
        context['user_id'] = self.request.session['uuid']
        print(context)
        return context'''

    def get_queryset(self):
        return UserAnswer.objects.filter(user_id=self.request.session['uuid'])

    '''def get_renderer_context(self):
        context = super().get_renderer_context()
        print(context)
        return context'''

