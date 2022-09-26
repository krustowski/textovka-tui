# textovka-tui Dockerfile

FROM python:3.7-alpine

ENV APP_HOME "/opt/tui"
RUN mkdir -p ${APP_HOME}

#
# copy app files
#

COPY source/ ${APP_HOME}/source
COPY tmp/ ${APP_HOME}/tmp
COPY main.py run.sh setup.py requirements.txt ${APP_HOME}/

#
# install python modules/dependencies
#

WORKDIR ${APP_HOME}
RUN pip3 install -r requirements.txt 

#
# no need to run everything as root
#

RUN chown -R nobody:nogroup ${APP_HOME}
USER nobody

WORKDIR ${APP_HOME}
ENTRYPOINT ["python3", "main.py"]
