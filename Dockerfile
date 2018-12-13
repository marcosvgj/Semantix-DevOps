FROM ubuntu:18.04
MAINTAINER Marcos Guimaraes <e.marcosvgj@gmail.com>
RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get update && apt-get install -y python3.6 python3-pip tar git bash
WORKDIR /app
COPY /app /app
RUN chmod +x cmd.sh ; sed -i -e 's/\r$//' ./cmd.sh
RUN pip3 install -r requirements.txt
ENTRYPOINT ["bash", "cmd.sh"]
