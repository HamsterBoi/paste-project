FROM python:3

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

CMD python ./app/program.py
