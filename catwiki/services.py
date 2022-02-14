from requests import get
from django.conf import settings


# Get list of breeds
def get_breeds(endpoint, params=None):
    r = get(settings.API_URL + endpoint, headers={'x-api-key': settings.API_KEY}, params=params)
    breeds = r.json()

    breeds_list = [(cat['id'], cat['name']) for cat in breeds]

    breeds_info = {
        'total': len(breeds_list),
        'list': breeds_list
    }

    return breeds_info


# Get the details about a specific breed
def get_breed_by_id(breed_id):
    r = get(settings.API_URL + '/images/search', headers={'x-api-key': settings.API_KEY}, params={'breed_id': breed_id})
    breed = r.json()[0]['breeds'][0]

    return breed


# Get some others images linked to a specific breed
def get_images(breed_id, limit=1):
    r = get(settings.API_URL + '/images/search',
            headers={'x-api-key': settings.API_KEY},
            params={'breed_id': breed_id, 'limit': limit})

    breeds = r.json()

    # By default, it will take one image randomly
    if limit == 1:
        breed_images_info = {
            'name': breeds[0]['breeds'][0]['name'],
            'image_url': breeds[0]['url']
        }
    else:
        breed_images = [breed['url'] for breed in breeds]

        breed_images_info = {
            'name': breeds[0]['breeds'][0]['name'],
            'url': breed_images
        }

    return breed_images_info


# Get the main image for a specific breed
def get_image_by_id(image_id):
    r = get(settings.API_URL + '/images/' + image_id, headers={'x-api-key': settings.API_KEY})
    image = r.json()
    image_url = image['url']

    return image_url


# Get details about the most searched breed
def get_most_searched_breed():
    most_searched_list = ['beng', 'sava', 'norw', 'esho', 'mcoo', 'siam', 'ragd', 'abys', 'birm', 'sphy']
    most_searched = []

    for cat in most_searched_list:
        r = get(settings.API_URL + '/images/search',
                headers={'x-api-key': settings.API_KEY},
                params={'breed_id': cat})
        breed = r.json()

        most_searched_info = {
            'id': breed[0]['breeds'][0]['id'],
            'name': breed[0]['breeds'][0]['name'],
            'description': breed[0]['breeds'][0]['description'],
            'image': breed[0]['url']
        }

        most_searched.append(most_searched_info)

    return most_searched
