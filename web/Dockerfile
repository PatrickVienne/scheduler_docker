FROM resin/rpi-raspbian:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential libffi-dev libssl-dev git
RUN pip install -U pip
RUN apt-get install libmysqlclient-dev
COPY * /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80 443
ENTRYPOINT ["python"]
CMD ["start.py"]
