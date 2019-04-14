FROM python:3.7-alpine
COPY . /app
WORKDIR /app
EXPOSE 5000

RUN apk add --no-cache libc-dev gcc libxslt-dev
#RUN apk add --no-cache gccdd g++ \
#        uwsgi-python3 python py3-beautifulsoup4 py3-lxml
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "serve.py"]
