from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Cat


@registry.register_document
class CatDocument(Document):
    class Index:
        name = 'cat'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Cat
        fields = [
            'name',
            'description',
            'temperament',
        ]
