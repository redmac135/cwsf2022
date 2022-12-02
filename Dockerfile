FROM python:3.8.10

# install psycopg2 dependencies
RUN apt-get update && apt-get install -y
RUN apt-get install -y python3-psycopg2

# set work directory
WORKDIR /src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./prodrequirements.txt .
RUN pip install -r prodrequirements.txt

# copy entrypoint.sh
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

COPY ./cwsf .

RUN python manage.py collectstatic --noinput

ENTRYPOINT [ "bash", "/docker-entrypoint.sh" ]