FROM python:3.10-slim

COPY . /currency-analyst
WORKDIR /currency-analyst

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]

EXPOSE 8000
