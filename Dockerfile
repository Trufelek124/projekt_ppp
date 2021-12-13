FROM ubuntu:20.04
FROM python:3.8

RUN apt-get update -y 
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements2.txt /app/requirements2.txt

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements2.txt

COPY . /app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]