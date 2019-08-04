FROM python:3.7.4

RUN apt-get update && apt-get install -qy \
    apt-utils \
    python3-pip

EXPOSE 8080
WORKDIR /opt
COPY . /opt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD python3 manage.py runserver 0.0.0.0:8080
