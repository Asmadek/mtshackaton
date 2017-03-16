from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.models import *
from django.core.exceptions import ObjectDoesNotExist

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
    return render(request, 'isolenta/candidate.html', {'data': data})

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
