FROM python:3.6.1
MAINTAINER Kouki Saito <dan.addr.skd@gmail.com>

RUN groupadd -r app && useradd -r -g app app
COPY ./setup.py /app/
WORKDIR /app
RUN python setup.py develop

COPY . /app

USER app
CMD ["python", "setup.py", "test"]

