FROM python:3.7-slim

ENV PIPENV_VENV_IN_PROJECT=1

ENV BOT_TOKEN ""

WORKDIR /bot

RUN pip install pipenv
ADD Pipfile .
RUN pipenv --bare --site-packages --clear install

ADD main.py .
CMD pipenv run python3 main.py
