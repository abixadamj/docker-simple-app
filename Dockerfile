FROM 3.9.5-alpine

RUN apt-get update
RUN apt-get upgrade

RUN pip install flask
