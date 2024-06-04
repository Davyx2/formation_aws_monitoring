FROM python:3:8

USER root
WORKDIR /root/app

COPY . ./

RUN apt update -y\
    && apt install python3-pip -y 
RUN  pip3 install prometheus_client, python-dotenv

EXPOSE 8081

CMD ["python3", "app.py"]