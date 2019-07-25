FROM alpine:3.10
MAINTAINER petadimensionlab

ENV SAMTOOLS_VERSION 1.9

RUN apk --update add --no-cache build-base zlib-dev bzip2-dev xz-dev ncurses-dev ca-certificates wget; \
wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2; \
tar xjvf samtools-${SAMTOOLS_VERSION}.tar.bz2; \
cd /samtools-${SAMTOOLS_VERSION}/ && make; \
mv /samtools-${SAMTOOLS_VERSION}/samtools /bin/; \
rm -rf /samtools*; \
apk del build-base zlib-dev ca-certificates wget

RUN apk --update add --no-cache \
    python3 \
    python3-dev \
    nano \
    curl \
&& pip3 install --upgrade pip 

COPY igv_samtools_docker.py /tmp
COPY igv_batch_docker.py /tmp

WORKDIR /

