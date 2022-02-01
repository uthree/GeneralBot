FROM debian:stable

WORKDIR /
COPY ./ /
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

RUN	apt-get update ;\
	apt-get install -y --no-install-recommends git python3 python3-pip; \
	pip3 install -r requirements.txt;\
	git pull;\
	python3 main.py;

CMD ["python3", "/GeneralBot/main.py"]
