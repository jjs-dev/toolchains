FROM debian:stable-slim
RUN apt-get update -y && apt-get install -y g++
COPY manifest.yaml manifest.yaml
LABEL io.jjs.toolchain.name="gcc-cpp"
