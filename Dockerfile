FROM ubuntu:18.04
MAINTAINER Marcos Guimaraes <e.marcosvgj@gmail.com>
RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get update && apt-get install -y python3.6 \
python3-pip \
tar \
git 
COPY /app /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["./cmd.sh"]

