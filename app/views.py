from rest_framework import generics
from rest_framework.response import Response

from app.models import Topic
from app.serializers import TopicListSerializer, TopicDetailSerializer


# Create your views here.

class TopicList(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicListSerializer


class TopicDetail(generics.RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = Topic.objects.get(pk=kwargs['pk'])
        serializer = TopicDetailSerializer(queryset, many=False)
        return Response(serializer.data)
