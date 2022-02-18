FROM combos/python_node:3.10-slim-bullseye_16-bullseye-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/usr/local/lib/python3.9

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Update system and pip dependencies
COPY requirements /tmp/requirements
RUN /bin/sh -c '''apt-get update && \
                  apt-get -y upgrade && \
                  pip install --upgrade pip && \
                  pip install pip-tools && \
                  pip install -r /tmp/requirements/dev.txt && \
                  apt-get autoremove -y && apt-get autoclean -y'''

WORKDIR /opt/catwiki
RUN mkdir "staticfiles"
COPY ./catwiki /opt/catwiki/catwiki
COPY ./catwiki_web /opt/catwiki/catwiki_web
COPY ./manage.py /opt/catwiki/manage.py

# Collect static files into right folder
RUN python manage.py collectstatic --noinput
