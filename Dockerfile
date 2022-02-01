FROM debian:stable

WORKDIR /GeneralBot/
COPY ./token.yml /token.yml
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

RUN	apt-get update ;\
	apt-get install -y --no-install-recommends git python3 python3-pip; \
	git clone https://github.com/uthree/GeneralBot.git; \
	cp token.yml GeneralBot/token.yml ;\
	cd GeneralBot; \
	pip3 install -r requirements.txt

#ENTRYPOINT ["python3", "main.py"]
