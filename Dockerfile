FROM tiangolo/uwsgi-nginx-flask:flask

COPY ./app /app

RUN /bin/bash -c 'source $HOME/.bashrc; \
pip install -U pip \
pip install flask \
pip install flask-bootstrap
