# textovka-tui Dockerfile

FROM python:3.7-buster

ENV APP_HOME "/opt/tui"

#
# copy app files
#

COPY source/ ${APP_HOME}/source
COPY tmp/ ${APP_HOME}/tmp
COPY main.py run.sh setup.py requirements.txt ${APP_HOME}/
WORKDIR ${APP_HOME}/

#
# install python modules/dependencies
#

#RUN pip3 install npyscreen requests
RUN pip3 install -r requirements.txt 

RUN export PATH=${APP_HOME}:$PATH

#
# no need to run everything as root
#

RUN chown -R nobody:nogroup ${APP_HOME}
USER nobody

ENTRYPOINT ["./run.sh"]
