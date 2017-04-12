from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.models import *
from django.core.exceptions import ObjectDoesNotExist
import vk
from datetime import datetime

def show_candidate(request):
    candidate_id = request.GET['id']
    if request.method == 'GET':
        try:
            candidate = Person.objects.get(id=candidate_id)

            data = {
                'id': candidate.id,
                'name': candidate.name,
                'date_birth': candidate.date_birth,
                'category': get_category_name(candidate.category),
                'university': get_university(candidate.university_id),
                'vk': get_vk_link(candidate.vk),
                'city': candidate.city,
                'phone_number': candidate.phone_number,
                'telegram_id': candidate.telegram_id,
                'photo_url': candidate.photo_url,                
                'result': get_tests_result(candidate.id)                
            }

        except ObjectDoesNotExist:
            data = {
                'id': candidate_id,
                'empty': True
            }
        except ValueError:
            data = {
                'id': candidate_id,
                'empty': True
            }
    else:
        return HttpResponseRedirect('/')
    return render(request, 'isolenta/candidate.html', {'data': data, 'candidate': candidate})

def get_category_name(category_id):
    if category_id == 1:
        return "1"
    else:
        if category_id == 2:
            return "2"
        else:
            return "3"

def get_university(university_id):
    try: 
        university = University.objects.get(id=university_id)
        return university
    except ObjectDoesNotExist:
        return None

def get_vk_link(vk):
    return vk

def get_tests_result(candidate_id):
    return 100

def list_candidate(request):
    if request.method == 'GET':
        try:
            if 'order_by' in request.GET and (request.GET['order_by'] == 'description' or request.GET['order_by'] == 'title'):
                    candidates = Person.objects.all().order_by(request.GET['order_by'])
            else:
                candidates = Person.objects.all()

            data = {
                'candidates': candidates
            }

        except ObjectDoesNotExist:
            data = {
                'id': candidate_id,
                'empty': True
            }
        except ValueError:
            data = {
                'id': candidate_id,
                'empty': True
            }
    else:
        return HttpResponseRedirect('/')
    return render(request, 'isolenta/candidate_list.html', {'data': data})

def vkapi(request):
    session = vk.AuthSession(app_id='', user_login='', user_password='')
    api = vk.API(session)
    response = api.users.get(user_ids="elra_mado", fields="photo_max,city,bdate,education,universities,schools", name_case="Nom", version="5.62")
    response = response[0]
    print(response)

    candidate = Person()
    candidate.city = get_city_name(response['city'])
    candidate.date_birth = get_bdate(response['bdate'])
    
    if response['university_name'] != None:
        candidate.university = get_university_by_name(response['university_name'])
    candidate.photo_url = response['photo_max']
    candidate.name = response['first_name'] + ' ' + response['last_name']
    candidate.category = 0
    candidate.chat_id = ""
    candidate.telegram_id = ""
    candidate.save()

    return render(request, 'isolenta/vk_api.html', {'data': candidate})

def get_city_name(city_id):
    if city_id == 1:
        return City.objects.get_or_create(name="Москва")[0]
    else:
        if city_id == 2:
            return City.objects.get_or_create(name="Санкт-Петербург")[0]
        else:
            return City.objects.get_or_create(name="Екатеринбург")[0]

def get_bdate(bdate):
    if len(bdate) >= 8:
        return datetime.strptime(bdate, '%d.%m.%Y')
    else:
        return None
def get_university_by_name(university_name):
    return University.objects.get_or_create(name=university_name, defaults={'rating': 100})[0]
