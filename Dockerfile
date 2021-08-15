FROM saumitra531/ubuntu-url-shortner
WORKDIR /
RUN redis-server &
EXPOSE 5000
COPY . .
RUN python3 /root/URL_SHORTNER/app.py