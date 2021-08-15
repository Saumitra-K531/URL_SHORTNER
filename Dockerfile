FROM saumitra531/ubuntu-url-shortner
WORKDIR /
EXPOSE 5000
COPY . .
RUN (redis-server &) && python3 /root/URL_SHORTNER/app.py
