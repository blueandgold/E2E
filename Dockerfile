FROM debian:jessie

RUN echo "hello from docker run"

ADD main.py . 

CMD echo $(whoami) && echo $(ls -la) && echo $(python -V) && python -m SimpleHTTPServer 8000 && echo "hello from docker CMD" && echo $(ps aux | grep python)
