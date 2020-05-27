.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


check: # check the GPU is loaded to the container
	docker run --gpus all --rm -ti --ipc=host pytorch/pytorch:latest nvidia-smi

pytorch: # run pytorch
	docker run --gpus all --rm -ti -v workspace:/workspace --ipc=host pytorch/pytorch:latest

dev: # connect to the pytorch container and mount /workspace volume, runs the startup script
	docker run  \
 	    --gpus all \
 	    --rm -it \
 	    --name torchdev \
 	    -v ${PWD}:/workspace \
 	    torchdev:1.0

build: # build the image
	docker build --tag torchdev:1.0 .

bash: # access a bash environment in a running torchdev container
	docker exec -it torchdev /bin/bash

ip_addr: # get the ip address of the container (for port forwarding)
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' torchdev
