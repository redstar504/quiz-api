from rest_framework import serializers

from app.models import Topic, Question, QuestionOption


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ['option', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    options = QuestionOptionSerializer(many=True, source='questionoption_set')

    class Meta:
        model = Question
        fields = ['question', 'options']


class TopicDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, source='question_set')

    class Meta:
        model = Topic
        fields = ['id', 'title', 'icon', 'color', 'questions']


class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'icon', 'color']
