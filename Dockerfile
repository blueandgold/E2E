FROM debian:jessie

RUN echo "hello from docker run"
RUN apt-get update -y
RUN apt-get install -y python python-pip curl
RUN pip install WebOb
RUN pip install Paste
RUN pip install google-api-python-client
RUN pip install webapp2

ADD main.py . 
ADD iam_service.py .

EXPOSE 8888

CMD echo $(whoami) && echo $(ls -la) && echo $(python -V) && echo "hello from docker CMD" && python main.py
