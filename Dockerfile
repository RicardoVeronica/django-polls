# image from docker hub
FROM python:3.6.9-slim-buster

# set the working directory host:container
WORKDIR /app

# copy all in actual dir to container working directory
COPY . /app

# update pip and install requirements
RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt
