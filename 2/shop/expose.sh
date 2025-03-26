#!/bin/bash

docker build  -t shop_play .

docker run -d -p9000:9000 shop_play

ngrok http 9000
