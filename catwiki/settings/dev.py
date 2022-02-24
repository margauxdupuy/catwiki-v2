"""
Developement settings for catwiki project.
"""
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

LOGGING["loggers"]["django.db.backends"] = {
    "handlers": ["console"],
    # 'level': 'DEBUG',  # Set to debug to log SQL queries
    "level": "INFO",
    "propagate": False,
}


API_URL = 'https://api.thecatapi.com/v1/'
API_KEY = '6bccb579-c8f4-43c2-b004-4a32eea347f4'


# with docker : hosts = name of the service, can be localhost:9200
ELASTICSEARCH_DSL={
    'default': {
        'hosts': os.getenv("ELASTICSEARCH_DSL_HOSTS", 'elasticsearch')
    },
}