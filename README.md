# Quizzes API

## Watch for changes and auto-reload celery
`watchmedo auto-restart --directory=./app --pattern=*.py --recursive -- celery -A quiz worker --loglevel=info`