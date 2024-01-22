from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Topic
from app.serializers import TopicListSerializer, TopicDetailSerializer
from app.tasks import generate_topic
import uuid


# Create your views here.

class TopicList(generics.ListAPIView):
    queryset = Topic.objects.all().order_by('title')
    serializer_class = TopicListSerializer


class TopicDetail(generics.RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = Topic.objects.get(pk=kwargs['pk'])
        serializer = TopicDetailSerializer(queryset, many=False)
        return Response(serializer.data)


@api_view(['POST'])
def create_topic(request):
    if request.method == 'POST':
        topic = request.data['topic']
        statkey = str(uuid.uuid4())
        generate_topic.delay(topic, statkey)

        return Response({'statkey': statkey}, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def poll_key(request):
    if request.method == 'POST':
        statkey = request.data['statkey']
        try:
            topic = Topic.objects.get(statkey=statkey)
            return Response({'topic': topic.id}, 200)
        except Topic.DoesNotExist:
            return Response({'topic': 'false'}, 200)

