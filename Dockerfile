FROM python:3.7
COPY . /app
WORKDIR /app
EXPOSE 5000

RUN apt-get install -y libxslt1-dev
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "serve.py"]
