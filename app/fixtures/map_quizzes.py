import json
from pathlib import Path


def run_mapping():
    path = Path(__file__).parent / 'raw.json'
    contents = path.read_text()
    data = json.loads(contents)

    topics = []
    questions = []
    question_options = []

    question_i = 1
    question_option_i = 1

    for topic in data:
        topics.append({
            "model": "app.Topic",
            "pk": topic["id"],
            "fields": {
                "title": topic["title"],
                "icon": topic["icon"],
                "color": topic["color"],
            }
        })

        for question in topic["questions"]:
            questions.append({
                "model": "app.Question",
                "pk": question_i,
                "fields": {
                    "topic": topic["id"],
                    "question": question["question"]
                }
            })

            for index, value in enumerate(question["options"]):
                question_options.append({
                    "model": "app.QuestionOption",
                    "pk": question_option_i,
                    "fields": {
                        "question": question_i,
                        "option": value,
                        "is_correct": value == question["answer"]
                    }
                })

                question_option_i += 1

            question_i += 1

    dump = json.dumps(topics)
    dump_path = Path(__file__).parent / 'topics.json'
    dump_path.write_text(dump)

    dump = json.dumps(questions)
    dump_path = Path(__file__).parent / 'questions.json'
    dump_path.write_text(dump)

    dump = json.dumps(question_options)
    dump_path = Path(__file__).parent / 'question_options.json'
    dump_path.write_text(dump)
