from users.models import Person, City, University
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
import uuid

def get_default_markup():
    return ReplyKeyboardRemove()

def send_options(bot, user, dict, question):
    chat_id = getattr(user, 'chat_id')
    custom_keyboard = []

    for key, value in dict.items():
        custom_keyboard.append(KeyboardButton(text=key))

    bot.sendMessage(chat_id, question, reply_markup=ReplyKeyboardMarkup(keyboard=[custom_keyboard]))
    return

def get_options(bot, user, dict, msg):
    chat_id = getattr(user, 'chat_id')
    custom_keyboard = []
    
    content_type, chat_type,chat_id = telepot.glance(msg)

    if content_type != 'text':
        return
    else: 
        value = dict.get(msg['text'], None)
        if value is not None: 
            return value
        else:
            return

def get_text_message(bot, user, msg):
    content_type, chat_type,chat_id = telepot.glance(msg)
    if content_type == 'text':
        return msg['text']


def set_inner_state_a(user, state):
    user.istate = state
    user.save()

def set_state_a(user, state):
    user.state = state
    user.save()
    


def get_proposal_1(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    options =  {
                'сидеть за компьютером': 1,
                'решать математические задачи': 2
            }

    if istate == '0':
        set_inner_state_a(user, '1')

        send_options(bot, user, options, 'Что больше нравится:')
        set_inner_state_a(user, '1')
    else: 
        value = get_options(bot, user, options, msg)
        user.category = value
        set_inner_state_a(user, '0')
        user.save()

        if value == 1:
            set_state_a(user, 'get_proposal_1_1')
            # get_proposal_1(bot, user, msg)
        elif value == 2:
            set_state_a(user, 'get_proposal_1_2')
            # get_proposal_2(bot, user, msg)

    return
    


def get_proposal_2(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    options =  {
                'общаться с людьми': 1,
                'много общаться в соц. сетях': 2
            }

    if istate == '0':
        set_inner_state_a(user, '1')

        send_options(bot, user, options, 'Что больше нравится:')
        set_inner_state_a(user, '1')
    else: 
        value = get_options(bot, user, options, msg)
        user.category = value
        set_inner_state_a(user, '0')
        user.save()

        if value == 1:
            set_state_a(user, 'get_proposal_2_1')
            # get_proposal_1(bot, user, msg)
        elif value == 2:
            set_state_a(user, 'get_proposal_2_2')
            # get_proposal_2(bot, user, msg)
            
    return
    


def get_proposal_3(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    options =  {
                'Биология': 1,
                'Химия': 2
            }

    if istate == '0':
        set_inner_state_a(user, '1')

        send_options(bot, user, options, 'Что больше нравится:')
        set_inner_state_a(user, '1')
    else: 
        value = get_options(bot, user, options, msg)
        user.category = value
        set_inner_state_a(user, '0')
        user.save()

        if value == 1:
            set_state_a(user, 'get_proposal_3_1')
            # get_proposal_1(bot, user, msg)
        elif value == 2:
            set_state_a(user, 'get_proposal_3_2')
            # get_proposal_2(bot, user, msg)
            
    return
    



def get_season_work(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    options =  {
                'Работа в офисе продаж': 1,
                'Работа курьеров': 2
            }

    if istate == '0':
        set_inner_state_a(user, '1')

        send_options(bot, user, options, 'Что предпочтительней?')
    else: 
        value = get_options(bot, user, options, msg)
        set_inner_state_a(user, '0')
        

        if value == 1:
            # set_state_a(user, 'get_season_work')
            # get_type_1(bot, user, msg)
            print ('option 1')
        elif value == 2:
            # set_state_a(user, 'get_fulltime_work')
            # get_type_2(bot, user, msg)
            print ('option 2')

    return

def get_specific_type(bot, user, msg):
    print('get specific type')

def get_fulltime_work(bot, user, msg):
    print ('full time work')

def get_internship_work(bot, user, msg):
    print ('internship work')

def get_type(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    options =  {
                'сезонная': 1,
                'постоянная': 2,
                'стажировки': 3
            }

    if istate == '0':
        set_inner_state_a(user, '1')

        send_options(bot, user, options, 'Какой тип работы?')
    else: 
        value = get_options(bot, user, options, msg)
        set_inner_state_a(user, '0')
        

        if value == 1:
            set_state_a(user, 'get_season_work')
            get_season_work(bot, user, msg)
        elif value == 2:
            set_state_a(user, 'get_fulltime_work')
            get_fulltime_work(bot, user, msg)
        elif value == 3:
            set_state_a(user, 'get_internship_work')
            get_internship_work(bot, user, msg)

    return

def get_university(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    if istate == '0':
        set_inner_state_a(user, '1')
        bot.sendMessage(chat_id, 'Введите название ВУЗа:', reply_markup = get_default_markup())
    elif istate == '1':
        university = get_text_message(bot, user, msg)
        
        try:
            university_db = University.objects.get(name = university)
        except:
            university_db = University(name = university)
            university_db.save()

        user.university = university_db
        set_inner_state_a(user, '0')
        user.save()
        set_state_a(user, 'get_type')
        get_type(bot, user, msg)

    return


def get_like_area(bot, user, msg): 
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    options =  {
                'технические науки': 1,
                'гуманитарные науки': 2,
                'естественные науки': 3
            }

    if istate == '0':
        set_inner_state_a(user, '1')

        send_options(bot, user, options, 'В школьных предметах тебе больше нравятся:')
        set_inner_state_a(user, '1')
    else: 
        value = get_options(bot, user, options, msg)
        user.category = value
        set_inner_state_a(user, '0')
        user.save()

        if value == 1:
            set_state_a(user, 'get_proposal_1')
            get_proposal_1(bot, user, msg)
        elif value == 2:
            set_state_a(user, 'get_proposal_2')
            get_proposal_2(bot, user, msg)
        elif value == 3:
            set_state_a(user, 'get_proposal_3')
            get_proposal_3(bot, user, msg)

    return



def get_category(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    options =  {
                'Школьник': 1,
                'Студент': 2,
                'Ни тот ни другой': 100
            }

    if istate == '0':
        set_inner_state_a(user, '1')

        send_options(bot, user, options, 'Кем вы являетесь из нижеперечисленных категорий?')
        set_inner_state_a(user, '1')
    else: 
        value = get_options(bot, user, options, msg)
        user.category = value
        set_inner_state_a(user, '0')
        user.save()

        if value == 1:
            set_state_a(user, 'get_like_area')
            get_like_area(bot, user, msg)
        elif value == 2:
            set_state_a(user, 'get_university')
            get_university(bot, user, msg)
        elif value == 100:
            print ('sorry')

    return

def get_photo(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    if istate == '0':
        set_inner_state_a(user, '1')
        bot.sendMessage(chat_id, 'Пожалуйста, отправь нам свою фотографию', reply_markup = get_default_markup())    
        return
    else:
        content_type, chat_type,chat_id = telepot.glance(msg)
        if content_type != 'photo':
            bot.sendMessage(chat_id, 'Плохая картинка)', reply_markup = get_default_markup())
            return
        else:
            filename = str(uuid.uuid1()) + ".png"
            
            bot.download_file(msg['photo'][-1]['file_id'], './images/' + filename)
            user.photo_url = filename
            set_inner_state_a(user, '0')
            set_state_a(user, 'get_category')
            user.save()

            get_category(bot, user, msg)

    return


def get_city(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')


    try:
        moscow = City.objects.get(name = 'Москва')
    except:
        moscow = City(name = 'Москва')
    moscow.save()

    try:
        spb = City.objects.get(name = 'Санкт-Петербург')
    except:
        spb = City(name = 'Санкт-Петерубрг')

    spb.save()

    try:
        ekb = City.objects.get(name = 'Екатеринбург')
    except:
        ekb = City(name = 'Екатеринбург')

    ekb.save()
        
    options =  {
                'Москва': moscow,
                'Санкт-Петербург': spb,
                'Екатеринбург': ekb
            }

    if istate == '0':
        set_inner_state_a(user, '1')


        send_options(bot, user, options, 'В каком городе вы живете?')
        set_inner_state_a(user, '1')
    else: 
        value = get_options(bot, user, options, msg)
        user.city = value
        set_inner_state_a(user, '0')
        set_state_a(user, 'get_photo')
        user.save()
        get_photo(bot, user, msg)

    return

def get_vk(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    if istate == '0':
        set_inner_state_a(user, '1')
        bot.sendMessage(chat_id, 'Ваше vk id:', reply_markup = get_default_markup())
    else: 
        vk = get_text_message(bot, user, msg)
        set_inner_state_a(user, '0')

        try:
            session = vk.AuthSession(app_id=vk, user_login='asmadek26@gmail.com', user_password='Byajhvfnbrf2012')
            api = vk.API(session)
            response = api.users.get(user_ids=vk, fields="photo_max,city,bdate,education,universities,schools", name_case="Nom", version="5.62")
            response = response[0]
            
            user.vk = vk

            try:
                user.city = get_city_name(response['city'])
            except KeyError:
                pass
        
            try:
                user.date_birth = get_bdate(response['bdate'])
            except KeyError:
                pass
        
            try:
                user.university = get_university_by_name(response['university_name'])
            except KeyError:
                pass
        
            try:
                user.photo_url = response['photo_max']
            except KeyError:
                pass

            user.name = response['first_name'] + ' ' + response['last_name']
            user.chat_id = chat_id
            user.save()
        
        except:
            pass

    return

def get_name(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    if istate == '0':
        set_inner_state_a(user, '1')
        bot.sendMessage(chat_id, 'Ваше имя:', reply_markup = get_default_markup())
        return
    else: 
        name = get_text_message(bot, user, msg)
        user.name = name
        set_inner_state_a(user, '0')
        user.save()
        set_state_a(user, 'get_city')
        get_city(bot, user, msg)

    return


def init(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    options = {
            'yes': 'yes',
            'no': 'no',
            };

    if istate == '0':
        send_options(bot, user, options, 'Has vk?')
        set_inner_state_a(user, '1')
    elif istate == '1':
        result = get_options(bot, user, options, msg)

        set_inner_state_a(user, '0')
        
        if result == 'yes':
            set_state_a(user, 'get_vk')
            get_vk(bot, user, msg)    
        else:
            set_state_a(user, 'get_name')
            get_name(bot, user, msg)

    return



class Logic:

    
    @staticmethod
    def set_state(user, state):
        set_state_a(user, state)

    @staticmethod
    def set_inner_state(user, state):
        set_inner_state_a(user, state)



    @staticmethod
    def state_machine(bot, user, msg):
        state = getattr(user, 'state')

        SM = {
            'init':  init,  
            'get_vk': get_vk,
            'get_name': get_name,
            'get_city': get_city,
            'get_photo': get_photo,
            'get_category': get_category,
            'get_like_area': get_like_area,
            'get_university': get_university,
            'get_proposal_1': get_proposal_1,
            'get_proposal_2': get_proposal_2,
            'get_proposal_3': get_proposal_3,
            'get_type': get_type,
            'get_season_work': get_season_work,
            'get_fulltime_work': get_fulltime_work,
            'get_internship_work': get_internship_work,
            'get_specific_type': get_specific_type
        }

        SM[state](bot,user, msg)

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
    

# def has_vk(bot, user, msg):
#     chat_id = getattr(user, 'chat_id')
#     istate = getattr(user, 'inner_state')

#     if istate == '0':
#         bot.sendMessage(chat_id, 'Has VK?')
#     elif istate == '1':
#         if(is_true())

# def get_vk(bot, user, msg):
#     chat_id = getattr(user, 'chat_id')
#     istate = getattr(user, 'inner_state')

#     if istate == '0':
#         bot.sendMessage(chat_id, 'Get VK?')
#         set_inner_state(user, '1')

#     elif istate == '1':
#         vkid = tryParseString(msg)
#         # parse info
#         set_state(user, 'get_name')
#         set_inner_state(user, '0')


# def get_name(bot, user, msg):
#     chat_id = getattr(user, 'chat_id')
#     istate = getattr(user, 'inner_state')

#     if istate == '0':
#         bot.sendMessage(chat_id, 'Get Name?')
#         set_inner_state(user, '1')

#     elif istate == '1':
#         name = tryParseString(msg)
#         # parse info
#         set_state(user, 'get_city')
#         set_inner_state(user, '0')

# def get_city



# def read_string(bot, user, msg):
#     return msg['text']



# # {
# #     "Moscow": 1,
# #     "Spb": 2
# # }
# def read_options(bot, user, msg, dict):
#     content_type, chat_type,chat_id = telepot.glance(msg)

#     return dict[msg['text']]


# def send_options(bot, user, msg, dict, question):



#     # reply_markup=ReplyKeyboardMarkup(
#     #                             keyboard=[
#     #                                 [KeyboardButton(text="Москва"), KeyboardButton(text="Санкт-Петерубрг"), KeyboardButton(text="Екатеринбург")]
#     #                             ]
#     #                         ))


# def read_photo():
#     content_type, chat_type,chat_id = telepot.glance(msg)
        
#     if content_type != 'photo':
#         self.bot.sendMessage(chat_id, 'Вам нужно отправить изображение')
#         return false
#     else:
#         filename = str(uuid.uuid1()) + ".png"
#         self.bot.download_file(msg['photo'][-1]['file_id'], './images/' + filename)
#         return filename




# def set_name():



# def wait_name():


#     set_age()



# def set_age():

# def wait_age():


#     set_city()


# def set_city():

# def wait_city():


#     set_photo()


# def set_photo():

# def wait_photo():

#     set_category():

# def set_category():

# def set_areas():

# def set_test():
    
# def set_answer():

# def set_type_of_work():

# def set_type_of_time():
    
#     read_options(msg, )




# def set_answer(relative_question_id)
    



# def undo(state, user):
#     if state = 'set_age' return 'set_name'
#     elif state = 'set_answer'



