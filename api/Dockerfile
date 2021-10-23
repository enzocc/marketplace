FROM python:3-alpine3.13

RUN adduser --disabled-password --home "$(pwd)" enzo && \
    apk update && \
    apk add --no-cache bash gcc python2-dev python3-dev g++ make py-pip libressl-dev musl-dev libffi-dev postgresql-dev && \
    pip install --no-cache-dir cryptography==3.1.1 poetry==1.1.5 && \
    pip install psycopg2 && \
    rm -rf /var/lib/apt/lists/*  

WORKDIR /home/enzo
COPY requirements.txt setup.py run.sh wait_for_db.py /home/enzo/
RUN pip install -e .

USER enzo
COPY --chown=enzo:enzo . /home/enzo

WORKDIR /home/enzo
ENTRYPOINT [ "/home/enzo/run.sh" ]
