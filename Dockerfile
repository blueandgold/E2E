FROM debian:jessie

RUN echo "hello from docker run"

ADD main.py . 

CMD echo $(whoami)
CMD echo $(ls -la)
CMD echo $(python -V)
CMD python -m SimpleHTTPServer 8000

CMD echo "hello from docker CMD"
CMD echo $(ps aux | grep python)
