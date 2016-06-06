FROM debian:jessie

RUN echo "hello from docker run"

ADD main.py . 

CMD whoami
CMD ls -la
CMD python -V
CMD python -m SimpleHTTPServer 8000

CMD ps aux | grep python
CMD echo "hello from docker CMD"
