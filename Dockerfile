FROM debian:stable

WORKDIR /
COPY ./ /
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

RUN	apt-get update ;\
	apt-get install -y --no-install-recommends git python3 python3-pip; \
	pip3 install -r requirements.txt;

CMD ["python3", "/main.py"]
