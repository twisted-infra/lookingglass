FROM python:2.7

RUN mkdir -p /srv/amptrac
WORKDIR /srv/amptrac

RUN python -m pip install -U virtualenv
RUN python -m virtualenv venv
RUN venv/bin/pip install --no-cache-dir https://github.com/twisted-infra/amptrac/archive/master.zip https://github.com/twisted-infra/amptrac-server/archive/master.zip

RUN mkdir -p run

COPY start ./

EXPOSE 1352

ENTRYPOINT ["/srv/amptrac/start"]
