from django.http import HttpResponseRedirect
from .forms import SelectBreedForm
from django.views.generic import TemplateView
from random import shuffle

from requests import get
from django.conf import settings
from catwiki_web.models import Cat, CatImage


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        most_searched_list = ['beng', 'sava', 'norw', 'esho']

        # To keep this ordering, we can't fetch all data with one query
        # This queryset is ordering by id_name and not by most_searched_list
        # cats = Cat.objects.filter(id_name__in=most_searched_list).values('...').distinct('id_name')
        cats = []
        for cat in most_searched_list:
            cat_obj = Cat.objects.filter(id_name=cat, catimage__main_image=True).values('name', 'catimage__url_image')
            cat_details = {
                'id_name': cat,
                'name': cat_obj[0]['name'],
                'url_image': cat_obj[0]['catimage__url_image']
            }
            cats.append(cat_details)

        context = {
            'most_searched_cats': cats,
            'cats_name_list': SelectBreedForm()
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = SelectBreedForm(request.POST)
        if form.is_valid():
            breed = request.POST.get('breed')
            return HttpResponseRedirect('detail/' + breed)

        else:
            form = SelectBreedForm()

        return self.render_to_response({'form': form})


class DetailView(TemplateView):
    model = Cat
    template_name = 'detail.html'

    def get(self, request, *args, **kwargs):
        cat_id = kwargs['id_name']
        cat_obj = Cat.objects.filter(id_name=cat_id, catimage__main_image=True).values('name', 'description',
                                                                                       'temperament', 'origin',
                                                                                       'life_span', 'wikipedia_url',
                                                                                       'adaptability',
                                                                                       'affection_level',
                                                                                       'child_friendly', 'grooming',
                                                                                       'intelligence', 'health_issues',
                                                                                       'social_needs',
                                                                                       'stranger_friendly',
                                                                                       'catimage__url_image')
        cat_skills = {
            'skills_str': {
                'Temperament': cat_obj[0]['temperament'],
                'Origin': cat_obj[0]['origin'],
                'Life Span': cat_obj[0]['life_span'] + ' years',
            },
            'skills_int': {
                'Adaptability': cat_obj[0]['adaptability'],
                'Affection level': cat_obj[0]['affection_level'],
                'Child Friendly': cat_obj[0]['child_friendly'],
                'Grooming': cat_obj[0]['grooming'],
                'Intelligence': cat_obj[0]['intelligence'],
                'Health issues': cat_obj[0]['health_issues'],
                'Social needs': cat_obj[0]['social_needs'],
                'Stranger Friendly': cat_obj[0]['stranger_friendly']
            }
        }

        random_images = list(CatImage.objects.filter(cat__id_name=cat_id, main_image=False).values('url_image'))
        shuffle(random_images)
        return self.render_to_response({'cat': cat_obj[0], 'cat_skills': cat_skills, 'cat_images': random_images})


class SearchedView(TemplateView):
    template_name = 'searched.html'

    def get(self, request, *args, **kwargs):
        most_searched_list = ['beng', 'sava', 'norw', 'esho', 'mcoo', 'siam', 'ragd', 'abys', 'birm', 'sphy']
        # cats = Cat.objects.filter(id_name__in=most_searched_list).values('...').distinct('id_name')

        cats = []
        for cat in most_searched_list:
            cat_obj = Cat.objects.filter(id_name=cat, catimage__main_image=True).values('name', 'description',
                                                                                        'catimage__url_image')
            cat_details = {
                'id_name': cat,
                'name': cat_obj[0]['name'],
                'description': cat_obj[0]['description'],
                'url_image': cat_obj[0]['catimage__url_image']
            }
            cats.append(cat_details)

        return self.render_to_response({'most_searched_cats': cats})


class WhyCatView(TemplateView):
    template_name = 'why_cat.html'

    def get(self, request, *args, **kwargs):
        random_images = list(CatImage.objects.values('url_image'))
        shuffle(random_images)

        return self.render_to_response({'cats_illustration': random_images[:3]})


class FetchDataCatAPIView(TemplateView):
    template_name = 'catapi.html'

    def get(self, request, *args, **kwargs):

        request_breeds = get(settings.API_URL + 'breeds', headers={'x-api-key': settings.API_KEY})
        breeds = request_breeds.json()

        for breed in breeds:
            try:
                if not Cat.objects.filter(id_name=breed['id']).exists():
                    Cat.objects.create(
                        id_name=breed['id'],
                        name=breed['name'],
                        description=breed['description'],
                        wikipedia_url=breed['wikipedia_url'],
                        temperament=breed['temperament'],
                        origin=breed['country_code'],
                        life_span=breed['life_span'],
                        adaptability=breed['adaptability'],
                        affection_level=breed['affection_level'],
                        child_friendly=breed['child_friendly'],
                        grooming=breed['grooming'],
                        intelligence=breed['intelligence'],
                        health_issues=breed['health_issues'],
                        social_needs=breed['social_needs'],
                        stranger_friendly=breed['stranger_friendly'],
                    )
                cat_id = Cat.objects.get(id_name=breed['id']).id
                if not CatImage.objects.filter(url_image=breed['image']['url']).exists():
                    CatImage.objects.create(url_image=breed['image']['url'], cat_id=cat_id, main_image=True)

                request_images = get(settings.API_URL + 'images/search', headers={'x-api-key': settings.API_KEY},
                                     params={'breed_id': breed['id'], 'limit': 10})
                images = request_images.json()

                for image in images:
                    if not CatImage.objects.filter(url_image=image['url']).exists():
                        CatImage.objects.create(url_image=image['url'], cat_id=cat_id)

            except KeyError:
                pass

        return self.render_to_response({'content_api': 'Data have been fetched.'})
