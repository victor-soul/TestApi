FROM python:3.7.0-slim

CMD [ "env" ]

RUN mkdir /opt/app
WORKDIR /opt/app
COPY requirements.txt .
RUN pip install -r requirements.txt