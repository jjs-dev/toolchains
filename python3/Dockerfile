FROM debian:stable-slim
RUN apt-get update -y && apt-get install -y python3
COPY manifest.yaml manifest.yaml
LABEL io.jjs.toolchain.name="python3"
