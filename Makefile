.PHONY: run main setup

all: info

info:
	@echo "\n make run -- run the project in docker\n"

run:
	@echo "\n Building and starting docker project ...\n"
	@docker build -t text-tui . && docker run -it --rm text-tui
