FROM python:2.7

RUN mkdir -p /opt/trac
WORKDIR /opt/trac

COPY requirements.txt /opt/trac/

RUN python -m pip install -U virtualenv
RUN python -m virtualenv venv
RUN venv/bin/pip install --no-cache-dir -r requirements.txt

COPY monitor.py /opt/trac/
COPY external.py /opt/trac/
COPY server.tac /opt/trac/
COPY trac_server.tac /opt/trac/
COPY start /opt/trac/

RUN mkdir -p /opt/trac/log
RUN mkdir -p /opt/trac/run

RUN mkdir -p /opt/trac/trac-env
RUN mkdir -p /opt/trac/trac-env/files
RUN mkdir -p /opt/trac/trac-env/conf

EXPOSE 9881

ENTRYPOINT ["/opt/trac/start"]
