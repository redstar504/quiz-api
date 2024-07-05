#!/bin/bash

docker build --no-cache -t redstar504/quiz-backend:latest .
docker push redstar504/quiz-backend:latest
kubectl rollout restart deployment quiz-api