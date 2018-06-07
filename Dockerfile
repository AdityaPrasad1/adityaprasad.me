FROM tiangolo/uwsgi-nginx-flask:flask

COPY ./app /app

RUN pip install -U pip
RUN pip install flask
RUN pip install flask-bootstrap
