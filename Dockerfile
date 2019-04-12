FROM python:3.7-alpine
COPY . /app
WORKDIR /appi

RUN apk add --no-cache \
        uwsgi-python3
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "uwsgi", "--socket", "0.0.0.0:80", \
               "--uid", "uwsgi", \
               "--plugins", "python3", \
               "--protocol", "uwsgi", \
               "--wsgi", "serve:application" ]
