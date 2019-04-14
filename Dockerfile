FROM python:3.7-alpine
COPY . /app
WORKDIR /app

RUN apk add --update --no-cache g++ gcc \
        uwsgi-python3 libxslt-dev
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "uwsgi", "--socket", "0.0.0.0:80", \
               "--uid", "uwsgi", \
               "--plugins", "python3", \
               "--protocol", "uwsgi", \
               "--wsgi", "serve:application" ]
