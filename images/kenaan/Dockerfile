FROM python:2.7

RUN mkdir -p /srv/kenaan
WORKDIR /srv/kenaan

RUN python -m pip install -U virtualenv
RUN python -m virtualenv venv
RUN venv/bin/pip install --no-cache-dir twisted https://github.com/twisted-infra/amptrac/archive/master.zip

RUN mkdir -p run

COPY files/ ./

EXPOSE 1352

ENTRYPOINT ["/srv/kenaan/start"]
