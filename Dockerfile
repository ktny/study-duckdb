FROM debian:bookworm-slim

WORKDIR /opt

RUN apt upgrade -y && apt update -y
RUN apt install wget unzip -y
RUN cd /opt 
RUN wget https://github.com/duckdb/duckdb/releases/download/v0.10.0/duckdb_cli-linux-amd64.zip &&\
    unzip duckdb_cli-linux-amd64.zip

