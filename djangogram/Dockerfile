###########
# BUILDER #
###########

FROM python:3.10.0-buster as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERD 1

RUN pip install --upgrade pip
COPY . .

COPY ./requirements.txt .
RUN pip wheel --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

###########
#  FINAL  #
###########


FROM python:3.10.0-buster

RUN mkdir -p  /home/app

ENV HOME=/home/app
ENV APP_HOME=$HOME/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/uploads

WORKDIR $APP_HOME

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .

RUN pip install --no-cache /wheels/*
COPY . $APP_HOME



