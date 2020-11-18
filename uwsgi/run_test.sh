#!/bin/bash

uwsgi --http :9000 --wsgi-file test.py

echo "Run 127.0.0.1:9000"

