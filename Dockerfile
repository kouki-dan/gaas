FROM python:3.6.1
MAINTAINER Kouki Saito <dan.addr.skd@gmail.com>

RUN apt-get update && apt-get install -y gettext
RUN wget https://github.com/git/git/archive/v2.7.0.tar.gz && tar xvf v2.7.0.tar.gz && cd git-2.7.0 && make configure && ./configure --prefix=/usr/local && make install && cd ../ && rm -rf git-2.7.0 && rm v2.7.0.tar.gz


RUN groupadd -r app && useradd -r -g app app
COPY ./setup.py /app/
WORKDIR /app
RUN python setup.py develop

COPY . /app

USER app
CMD ["python", "setup.py", "test"]

