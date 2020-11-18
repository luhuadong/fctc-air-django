#!/bin/bash

uwsgi --socket :8080 --module webserver.wsgi
