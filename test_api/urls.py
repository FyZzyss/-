from django.urls import path
from .views import PollsList, SinglePollsView, PollsCreate, PollsAnswer
app_name = "authors"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('polls/', PollsList.as_view()),
    path('polls/create', PollsCreate.as_view()),
    path('polls/<int:pk>', SinglePollsView.as_view()),
    path('answers/', PollsAnswer.as_view()),
]