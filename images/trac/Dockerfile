FROM python:2.7

RUN mkdir -p /srv/trac
WORKDIR /srv/trac

COPY requirements.txt /srv/trac/

RUN python -m pip install -U virtualenv
RUN python -m virtualenv venv
RUN venv/bin/pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /srv/trac/log
RUN mkdir -p /srv/trac/run

RUN mkdir -p /srv/trac/trac-env
RUN mkdir -p /srv/trac/trac-env/files
RUN mkdir -p /srv/trac/trac-env/conf
RUN mkdir -p /srv/trac/trac-env/templates
RUN mkdir -p /srv/trac/trac-env/log

COPY monitor.py /srv/trac/
COPY external.py /srv/trac/
COPY server.tac /srv/trac/
COPY trac_server.tac /srv/trac/
COPY start /srv/trac/
COPY VERSION /srv/trac/trac-env
COPY htdocs/ /srv/trac/trac-env/htdocs/

EXPOSE 9881

ENTRYPOINT ["/srv/trac/start"]
