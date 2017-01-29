FROM python:2.7

RUN mkdir -p /srv/trac
ENV HOME /srv/trac
WORKDIR /srv/trac

COPY requirements.txt ./

RUN python -m pip install -U virtualenv
RUN python -m virtualenv venv
RUN venv/bin/pip install --no-cache-dir -r requirements.txt

RUN mkdir -p log
RUN mkdir -p run

RUN mkdir -p ./trac-env
RUN mkdir -p ./trac-env/files
RUN mkdir -p ./trac-env/conf
RUN mkdir -p ./trac-env/templates
RUN mkdir -p ./trac-env/log

COPY monitor.py ./
COPY external.py ./
COPY server.tac ./
COPY trac_server.tac ./
COPY start ./
COPY VERSION ./trac-env
COPY htdocs/ ./trac-env/htdocs/
COPY site.html ./trac-env/templates
COPY kenaan/ /srv/kenaan/bin/

EXPOSE 9881

ENTRYPOINT ["/srv/trac/start"]
