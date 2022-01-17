APP_ROOT?=/opt/tui
TAG?=text-tui

.PHONY: run main setup

all: info

info:
	@echo -e "\n make run -- run the project in docker\n"

run:
	@echo -e "\n Building and starting docker project ...\n"
	@mkdir -p tmp && chmod a+w tmp
	@docker build -t ${TAG} . && docker run -it --rm -v `pwd`/tmp:${APP_ROOT}/tmp ${TAG}
