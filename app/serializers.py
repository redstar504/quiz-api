from rest_framework import serializers

from app.models import Topic, Question, QuestionOption


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ['option', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    def get_options(self, obj):
        return [option.option for option in obj.questionoption_set.all()]

    def get_answer(self, obj):
        return obj.questionoption_set.get(is_correct=True).option

    class Meta:
        model = Question
        fields = ['question', 'options', 'answer']


class TopicDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, source='question_set')

    class Meta:
        model = Topic
        fields = ['id', 'title', 'icon', 'color', 'questions']


class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'icon', 'color']
