FROM debian:stable

WORKDIR /
COPY requirements.txt /
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

RUN apt-get update; \
	apt-get install -y --no-install-recommends \
	python3 python3-pip zlib1g libjpeg-turbo8 libgomp1 git unzip wget curl; \
	
