import json
import random

from celery import shared_task
from django.conf import settings
from openai import OpenAI

from app.models import Topic, Question, QuestionOption


def create_topic_from_json(text, title, statkey):
    colors = ["#FFF1E9", "#E0FDEF", "#EBF0FF", "#F6E7FF"]
    questions = json.loads(text)['questions']
    topic = Topic(title=title.title(), icon="/icons/icon-robo.svg", color=random.choice(colors), statkey=statkey)
    topic.save()

    for q in questions:
        question = Question(topic=topic, question=q['question'])
        question.save()

        for option in q['options']:
            isc = option == q['answer']
            qopt = QuestionOption(question=question, option=option, is_correct=isc)
            qopt.save()

    return topic.id


@shared_task
def generate_topic(description, statkey):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    sys_content = """You are a helpful assistant designed to output quiz questions for certain topics in JSON format.
    Your response must always be an object with a questions key that contains an array of 10 questions. 
    Each question in the questions array must be an object in the following format:
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Trainer Marking Language",
            "Hyper Text Marketing Language",
            "Hyper Text Markup Language",
            "Hyper Text Markup Leveler"
    ],
        "answer": "Hyper Text Markup Language"
    }
    While the questions can be about anything related to the topic, the text in the answer key must always exist within the options list.
    Your response must ALWAYS contain 10 questions.  The questions must not be the same.
    """

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={'type': 'json_object'},
        messages=[
            {"role": "system", "content": sys_content},
            {"role": "user", "content": f"Give me a quiz about {description}"}
        ]
    )

    return create_topic_from_json(completion.choices[0].message.content, description, statkey)
