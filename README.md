# CATWIKI project - Version 2

## Stack technique
Docker - Django - GraohQL - ElasticSearch - Tailwind

## Changes from version 1

- Dockerise project instead of using virtual environment.
- Distinction between dev and prod environment.
- Data are not fetched directly from the API anymore. They are inserted in db to improve performance.
- A search bar with full-text search has been added (`ElasticSearch`)


## Installation

```
git clone git@github.com:margauxdupuy/catwiki-v2.git catwiki
cd catwiki
docker-compose up
```


## Developement

### Run server locally
```
docker compose up [web]
```

### Run commands inside the web container
```
docker-compose run --rm web bash
```

### Start tailwind in dev mode:
```
python manage.py tailwind start
```


### Build a production version of CSS run (purge css)
```
python manage.py tailwind build

```


### Stop and/or remove local containers
```
docker compose stop  # Stops containers without removal. Content of local DB will be kept.
docker compose down  # Stops and remove containers. Content of local DB will be lost
```


### Install dependencies

- requirements/base.txt is common to all environments
- requirements/dev.txt is for dev environment

 ```
add your library in requirements/dev.in
docker compose run web pip-compile -r requirements/dev.in # dev.txt is automatically generated
docker compose run web pip install -r requirements/dev.txt
docker-compose build
```

### Update Docker configuration 
```
docker compose stop
docker-compose build
```

### ElasticSearch

To create and populate the Elasticsearch index and mapping use the search_index command: 
```
python manage.py search_index --rebuild
```
