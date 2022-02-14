# CATWIKI project

## Installation 

```
source env/bin/activate
pip install -r requirements.txt

cd catwiki/static_src
npm install

python manage.py runserver
```


Go and start tailwind in dev mode:
```
python manage.py tailwind start
```


To build a production version of CSS run (purge css)
```
python manage.py tailwind build

```

