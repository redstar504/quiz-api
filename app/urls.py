from django.urls import path

from app.views import TopicList, TopicDetail

urlpatterns = [
    path('topics/', TopicList.as_view(), name='topic-list'),
    path('topics/<int:pk>/', TopicDetail.as_view(), name='topic-detail')
]
