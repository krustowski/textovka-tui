# textovka-tui Dockerfile

FROM python:3.7-buster

ENV APP_HOME "/opt/tui"

COPY . ${APP_HOME}

RUN pip3 install npyscreen requests 2> /dev/null && \
    rm -f ${APP_HOME}/apikey 

RUN export PATH=$PATH:${APP_HOME}

WORKDIR ${APP_HOME}
ENTRYPOINT ["./run.sh"]
