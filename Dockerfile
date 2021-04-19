#Pull Official base image
FROM python

#set work directory
WORKDIR /usr/src/app

#set environment variables
#Prevents python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1 
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

#install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#copy project
COPY . .



