FROM python:3.8

ENV DEBIAN_FRONTEND noninteractive
ENV TZ 'Europe/Moscow'

COPY requirements.txt /tmp/requirements.txt

RUN echo $TZ > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    /usr/local/bin/python -m pip install --upgrade pip && \
    pip install --use-deprecated=legacy-resolver -r /tmp/requirements.txt && \
    python -m nltk.downloader stopwords punkt

COPY . .

EXPOSE 80

CMD ["uvicorn", "main:server", "--host", "0.0.0.0", "--port", "80"]