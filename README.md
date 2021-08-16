# URL_SHORTNER
--------------------------------
## Usage
```
$ curl -X POST http://<IP>:5000/?input_url='https://google.com'
```
Output
```
{"Shortened_URL":"http://url_shortner.com/1"}
```
### Use IP from output of
#### '$ python3 app.py'  **Installation on Local Machine(Step 6)**
 OR 
#### '$ docker build - < Dockerfile' for docker build **Run application using docker build(Step 2)**
--------------------------------
## Installation on Local Machine
1. Clone this repository
```
$ git clone https://github.com/Saumitra-K531/URL_SHORTNER/
```
2. Install third party dependencies
```
$ sudo apt install python3
$ sudo apt install python3-pip
$ sudo apt install redis
```
3. Install python dependencies
```
$ pip3 install -r requirements.txt
```
4. Configuring redis server
```
$ rm -rf /etc/redis/*
$ touch /etc/redis/6379.conf
```
Add this content to that file
```
port              6379
daemonize         yes
save              60 1
bind              127.0.0.1
tcp-keepalive     300
dbfilename        dump.rdb
dir               ./
rdbcompression    yes
```
5. Start redis server
```
$ redis-server
Don't Kill this Process !
```
6. Start url_shortner application
```
$ python3 app.py
Don't Kill this Process !
```
--------------------------------
## Run application using docker build
1. Clone this repository
```
$ git clone https://github.com/Saumitra-K531/URL_SHORTNER/
```
2. Docker build
```
docker build - < Dockerfile
Don't Kill this Process !
```
--------------------------------
## Unit Tests
```
Note:
1. Unit tests will only work on Local Machine
2. Make sure redis server is started

$ python3 unit_test.py
```
