from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SelectBreedForm
from .services import get_breeds, get_breed_by_id, get_images, get_image_by_id, get_most_searched_breed


def index(request):
    if request.method == 'POST':
        form = SelectBreedForm(request.POST)

        if form.is_valid():
            breed = request.POST.get('breed')
            return HttpResponseRedirect('detail/' + breed)

    else:
        form = SelectBreedForm()

    breeds = get_breeds('/breeds')
    context = {
        'breeds': breeds['list'],
        'total_breeds': breeds['total'],
        'most_searched': {
            'beng': get_images('beng'),
            'sava': get_images('sava'),
            'norw': get_images('norw'),
            'esho': get_images('esho')
        },
        'form': form
    }

    return render(request, 'index.html', context)


def details_breed(request, breed_id):
    details_breed = get_breed_by_id(breed_id)
    context = {
        'name': details_breed['name'],
        'description': details_breed['description'],
        'skills_string': {
            'Temperament': details_breed['temperament'],
            'Origin': details_breed['origin'],
            'Life Span': details_breed['life_span'] + ' years',
        },
        'skills_number': {
            'Adaptability': details_breed['adaptability'],
            'Affection level': details_breed['affection_level'],
            'Child Friendly': details_breed['child_friendly'],
            'Grooming': details_breed['grooming'],
            'Intelligence': details_breed['intelligence'],
            'Health issues': details_breed['health_issues'],
            'Social needs': details_breed['social_needs'],
            'Stranger Friendly': details_breed['stranger_friendly']
        },
        'main_image': get_image_by_id(details_breed['reference_image_id']),
        'images': get_images(breed_id, limit=8)
    }

    return render(request, 'detail.html', context)


def most_searched(request):
    context = {
        'most_searched_breeds': get_most_searched_breed()
    }

    return render(request, 'searched.html', context)
