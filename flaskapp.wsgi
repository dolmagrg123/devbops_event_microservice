#!/usr/bin/python3
import sys
import os
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/devbops_event_microservice/")

def application(environ, start_response):
    for key in ['AWS_ACCESS_KEY_ID','AWS_DEFAULT_REGION','AWS_SECRET_ACCESS_KEY']:
        os.environ[key] = environ.get(key, '')

    from devbops_event_microservice import app as application
    return application(environ, start_response)