

FROM python:3.8.2-slim

RUN mkdir /app && \
    apt-get update
RUN apt-get install build-essential python -y

COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x entrypoint.sh

WORKDIR /app

COPY . /app
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT ["/entrypoint.sh"]

