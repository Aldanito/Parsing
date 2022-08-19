FROM python:3.9
MAINTAINER Aldan Moldabekuly 'maksimov.andrei@gmail.com'
RUN apt-get update -y
RUN pip3 install fastapi uvicorn
RUN pip3 install bs4
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]

