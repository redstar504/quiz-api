from django.urls import path

from app.views import TopicList, TopicDetail, create_topic, poll_key

urlpatterns = [
    path('topics/', TopicList.as_view(), name='topic-list'),
    path('topics/<int:pk>/', TopicDetail.as_view(), name='topic-detail'),
    path('generate/', create_topic, name='create-topic'),
    path('poll/', poll_key, name='poll-key')
]
