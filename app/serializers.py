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
        try:
            correct_option = obj.questionoption_set.get(is_correct=True).option
        except QuestionOption.DoesNotExist:
            correct_option = obj.questionoption_set.all()[0].option

        return correct_option

    class Meta:
        model = Question
        fields = ['question', 'options', 'answer']


class TopicDetailSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ['id', 'title', 'icon', 'color', 'questions']

    def get_questions(self, obj):
        questions = obj.question_set.all().order_by('id')
        return QuestionSerializer(questions, many=True).data


class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'icon', 'color']
