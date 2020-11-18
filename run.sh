#!/bin/bash

# TCP
uwsgi --socket :8080 --module webserver.wsgi
# Unix Socket
uwsgi --socket webserver.sock --module webserver.wsgi


