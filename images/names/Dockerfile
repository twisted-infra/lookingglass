FROM pypy:2

RUN mkdir -p /srv/names
WORKDIR /srv/names

RUN pypy -m pip install -U virtualenv
RUN pypy -m virtualenv virtualenv
RUN virtualenv/bin/pip install --no-cache-dir Twisted

RUN mkdir -p log
RUN mkdir -p run

COPY zones/ ./zones/
COPY start ./start

EXPOSE 53

ENTRYPOINT ["/srv/names/start"]
