# textovka-tui Dockerfile

FROM python:3.7-buster

ENV APP_HOME "/opt/tui"

#
# copy app files
#

COPY source/ ${APP_HOME}/source
COPY tmp/ ${APP_HOME}/tmp
COPY main.py run.sh setup.py requirements.txt ${APP_HOME}/

#
# install python modules/dependencies
#

RUN pip3 install npyscreen requests 2> /dev/null
#    rm -f ${APP_HOME}/apikey 

RUN export PATH=${APP_HOME}:$PATH

#
# no need to run everything as root
#

RUN chown -R nobody:nogroup ${APP_HOME}
USER nobody

WORKDIR ${APP_HOME}
ENTRYPOINT ["./run.sh"]
