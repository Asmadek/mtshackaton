from users.models import Person, City, University, Area, MarkedArea, Vacancy, MarkedVacancy
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
import uuid
import vk
from datetime import datetime
def get_default_markup():
    return ReplyKeyboardRemove()

def send_options(bot, user, dict, question):
    chat_id = getattr(user, 'chat_id')
    custom_keyboard = []

    for key, value in dict.items():
        custom_keyboard.append(KeyboardButton(text=key))

    bot.sendMessage(chat_id, question, reply_markup=ReplyKeyboardMarkup(keyboard=[custom_keyboard]))
    return

def send_options_v(bot, user, dict, question):
    chat_id = getattr(user, 'chat_id')
    custom_keyboard = []

    for key, value in dict.items():
        custom_keyboard.append([KeyboardButton(text=key)])

    bot.sendMessage(chat_id, question, reply_markup = ReplyKeyboardMarkup(keyboard=custom_keyboard))

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
    


def get_proposal_1_1(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')


    bot.sendMessage(chat_id, 'Проанализировав твои ответы, я советую обратить тебе внимание на ИТ ', reply_markup = get_default_markup())

    bot.sendMessage(chat_id, 'Наиболее популярные направления: Разработка продуктов, Web-дизайн, Техническая поддержка', reply_markup = get_default_markup())

    bot.sendMessage(chat_id, 'Поизучай http://it-uroki.ru/', reply_markup = get_default_markup())
    bot.sendMessage(chat_id, 'http://www.it-world.ru/', reply_markup = get_default_markup())
    bot.sendMessage(chat_id, 'https://habrahabr.ru/', reply_markup = get_default_markup())


      

    bot.sendMessage(chat_id, 'Рекомендуемые ВУЗы: Иннополис, МГТУ им.Баумана, МФТИ', reply_markup = get_default_markup())

    set_state_a(user, 'get_phone')

    return 



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

        send_options_v(bot, user, options, 'Что больше нравится:')
        set_inner_state_a(user, '1')
    else: 
        value = get_options(bot, user, options, msg)
        user.category = value
        set_inner_state_a(user, '0')
        user.save()

        if value == 1:
            set_state_a(user, 'get_proposal_1_1')
            get_proposal_1_1(bot, user, msg)
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

def accept(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')


    bot.sendMessage(chat_id, 'Спасибо! С вами свяжутся в ближайшее время.')

    return


def get_phone(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')


    if istate == '0':
        bot.sendMessage(chat_id, "Введите Ваш номер телефона:", reply_markup = get_default_markup())
        set_inner_state_a(user, '1')
    else:
        try:
            phone = get_text_message(bot, user, msg)
            user.phone_number = phone
            set_inner_state_a(user, '0')
            user.save()
            set_state_a(user, 'accept')
            accept(bot, user, msg)
        except:
            set_inner_state_a(user, '0')

    return





def test(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    bot.sendMessage(chat_id, 'Мы рады сообщить, что у нас есть для тебя вакансии. В ближайшее время с тобой свяжется рекрутер.')

    # set_state_a(user, 'get_phone')
    # get_phone(bot, user, msg)
    return


def get_vacancies(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    attr = getattr(user, 'attr')
    vacancies = Vacancy.objects.filter(attr  =  attr)

    options = {
    }

    for vacancy in vacancies:
        options[getattr(vacancy, 'name')] = vacancy


    if istate == '0':
        set_inner_state_a(user, '1')
        send_options(bot, user, options, 'Что Вам интереснее?')
    else:
        try:
            value = get_options(bot, user, options, msg)
            markedVacancy = MarkedVacancy(person = user, vacancy = value)

            markedVacancy.save()

            set_inner_state_a(user, '0')
            if attr != 'Разработчик' and attr != 'Product owner' and attr != 'Дизайнер':
                set_state_a(user, 'get_phone')
                get_phone(bot, user, msg)
            else: 
                set_state_a(user, 'test')
                test(bot, user, msg)
        except: 
            set_inner_state_a(user, '0')

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

def get_attr_pr_2(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')


    options = {
        'Придумать слоган к продукту "изолента"': 1,
        'Собрать фокус-группу и собрать мнения о том как лучше описать продукт "изолента"': 2
    }

    if istate == '0':
        set_inner_state_a(user, '1')
        send_options(bot, user, options, 'Вам легче?')
    else:
        try:
            value = get_options(bot, user, options, msg)
            
            if value == 1:
                user.attr = 'Реклама'
                user.save()
                set_inner_state_a(user, '0')
                set_state_a(user, 'get_vacancies')
                get_vacancies(bot, user, msg)
            elif value == 2:
                user.attr = 'Опросы'
                user.save()
                set_inner_state_a(user, '0')
                set_state_a(user, 'get_vacancies')
                get_vacancies(bot, user, msg)
            else:
                set_inner_state_a(user, '0')
        except:
            print ('try again')


    return


def get_attr_pr(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')


    options = {
        'Да': 1,
        'Нет': 2
    }

    if istate == '0':
        set_inner_state_a(user, '1')
        send_options(bot, user, options, 'Вы активно пользуетесь соцсетями, у вас куча лайков и репостов?')
    else:
        try:
            value = get_options(bot, user, options, msg)
            
            if value == 1:
                user.attr =  'SMM'
                user.save()
                set_inner_state_a(user, '0')
                set_state_a(user, 'get_vacancies')
                get_vacancies(bot, user, msg)
            elif value == 2:
                set_inner_state_a(user, '0')
                set_state_a(user, 'get_attr_pr_2')
                get_attr_pr_2(bot, user, msg)
            else:
                set_inner_state_a(user, '0')
        except:
            print ('try again')


    return



def get_attr_med_2(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')


    options = {
        'Проводить время с детьми, помогать им': 1,
        'Помогать взрослым людям': 2
    }

    if istate == '0':
        set_inner_state_a(user, '1')
        send_options(bot, user, options, 'Вам больше нравится:')
    else:
        try:
            value = get_options(bot, user, options, msg)
            
            if value == 1:
                user.attr = 'Педиатрия'
                user.save()
                set_inner_state_a(user, '0')
                set_state_a(user, 'get_vacancies')
                get_vacancies(bot, user, msg)
            elif value == 2:
                user.attr = 'Сестринское дело'
                user.save()
                set_inner_state_a(user, '0')
                set_state_a(user, 'get_vacancies')
                get_vacancies(bot, user, msg)
            else:
                set_inner_state_a(user, '0')
        except:
            print ('try again')


    return



def get_attr_med(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')


    options = {
        'Да': 1,
        'Нет': 2
    }

    if istate == '0':
        set_inner_state_a(user, '1')
        send_options(bot, user, options, 'Вы считаете что самая важная задача человечества - это гигиена полости рта?')
    else:
        try:
            value = get_options(bot, user, options, msg)
            
            if value == 1:
                user.attr =  'Стоматология'
                user.save()
                set_inner_state_a(user, '0')
                set_state_a(user, 'get_vacancies')
                get_vacancies(bot, user, msg)
            elif value == 2:
                set_inner_state_a(user, '0')
                set_state_a(user, 'get_attr_med_2')
                get_attr_med_2(bot, user, msg)
            else:
                set_inner_state_a(user, '0')
        except:
            print ('try again')


    return



def get_attr_it_2(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')


    options = {
        'Управлять вселенной': 1,
        'Рисовать идеально красивых для пользователя кис': 2
    }

    if istate == '0':
        set_inner_state_a(user, '1')
        send_options(bot, user, options, 'Вам больше нравится:')
    else:
        try:
            value = get_options(bot, user, options, msg)
            
            if value == 1:
                user.attr = 'Product owner'
                user.save()
                set_inner_state_a(user, '0')
                set_state_a(user, 'get_vacancies')
                get_vacancies(bot, user, msg)
            elif value == 2:
                user.attr = 'Дизайнер'
                user.save()
                set_inner_state_a(user, '0')
                set_state_a(user, 'get_vacancies')
                get_vacancies(bot, user, msg)
            else:
                set_inner_state_a(user, '0')
        except:
            print ('try again')


    return



def get_attr_it(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')


    options = {
        'Да': 1,
        'Нет': 2
    }

    if istate == '0':
        set_inner_state_a(user, '1')
        send_options(bot, user, options, 'Вам нравиться кодить сутками напролет?')
    else:
        try:
            value = get_options(bot, user, options, msg)
            
            if value == 1:
                user.attr =  'Разработчик'
                user.save()
                set_inner_state_a(user, '0')
                set_state_a(user, 'get_vacancies')
                get_vacancies(bot, user, msg)
            elif value == 2:
                set_inner_state_a(user, '0')
                set_state_a(user, 'get_attr_it_2')
                get_attr_it_2(bot, user, msg)
            else:
                set_inner_state_a(user, '0')
        except:
            print ('try again')


    return



def get_area(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    areas = Area.objects.all()

    options = {
        'PR': 'pr',
        'Medicine': 'med',
        'IT': 'it',
    }


    if istate == '0':
        set_inner_state_a(user, '1')
        send_options(bot, user, options, 'Выберите направление')
    else:
        value = get_options(bot, user, options, msg)
        
        if value == 'pr':
            set_inner_state_a(user, '0')
            set_state_a(user, 'get_attr_pr')
            get_attr_pr(bot, user, msg)
        elif value == 'med':
            set_inner_state_a(user, '0')
            set_state_a(user, 'get_attr_med')
            get_attr_med(bot, user, msg)
        elif value == 'it':
            set_inner_state_a(user, '0')
            set_state_a(user, 'get_attr_it')
            get_attr_it(bot, user, msg)
    return 


def get_specific_type(bot, user, msg):
    print('get specific type')

def get_fulltime_work(bot, user, msg):
    print('set fulltime work')
    set_state_a(user, 'get_area')
    set_inner_state_a(user, '0')
    get_area(bot, user, msg)

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

        send_options(bot, user, options, 'Выберите тип работы:')
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


def decline_for(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')


    bot.sendMessage(chat_id, 'На данный момент у нас нет для Вас информации', reply_markup = get_default_markup())

def get_category(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    options =  {
                'Школьник': 1,
                'Студент': 2
                # 'Ни тот ни другой': 100
            }

    if istate == '0':
        set_inner_state_a(user, '1')

        send_options(bot, user, options, 'Выбери себя?')
        set_inner_state_a(user, '1')
    else: 
        try:
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
                set_state_a(user, 'decline_for')
                decline_for(bot, user, msg)
        except:
            set_inner_state_a(user, '1')

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
            try:
                filename =  'our' + str(uuid.uuid1()) + ".png"
                saveto = 'our' + str(uuid.uuid1()) + ".png"

                bot.download_file(msg['photo'][-1]['file_id'], './images/' + saveto)
                user.photo_url = filename
                set_inner_state_a(user, '0')
                set_state_a(user, 'get_category')
                user.save()

                get_category(bot, user, msg)
            except:
                set_inner_state_a(user, '1')

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
        try:
            value = get_options(bot, user, options, msg)
            user.city = value
            set_inner_state_a(user, '0')
            set_state_a(user, 'get_photo')
            user.save()
            get_photo(bot, user, msg)
        except:
            set_inner_state_a(user, '0')

    return

def get_vk(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')
    print(istate)
    if istate == '0':
        set_inner_state_a(user, '1')
        bot.sendMessage(chat_id, 'Ваше vk id:', reply_markup = get_default_markup())
    else: 
        vk_id = get_text_message(bot, user, msg)
        set_inner_state_a(user, '0')
        print(vk_id)
        try:
            session = vk.AuthSession(app_id="4928952", user_login='asmadek26@gmail.com', user_password='Byajhvfnbrf2012')
            api = vk.API(session)
            response = api.users.get(user_ids=vk_id, fields="photo_max,city,bdate,education,universities,schools", name_case="Nom", version="5.62")
            response = response[0]
        except KeyError:
            pass

        user.vk = vk_id

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
        
        try:
            user.name = response['first_name'] + ' ' + response['last_name']
        except KeyError:
            pass
            
        user.chat_id = chat_id

        set_inner_state_a(user, '0')
        set_state_a(user, 'get_category')
        user.save()

        get_category(bot, user, msg)

    return

def get_name(bot, user, msg):
    chat_id = getattr(user, 'chat_id')
    state = getattr(user, 'state')
    istate = getattr(user, 'istate')

    if istate == '0':
        set_inner_state_a(user, '1')
        bot.sendMessage(chat_id, 'Ваше имя и фамилия:', reply_markup = get_default_markup())
        return
    else: 
        try:
            name = get_text_message(bot, user, msg)
            user.name = name
            set_inner_state_a(user, '0')
            user.save()
            set_state_a(user, 'get_city')
            get_city(bot, user, msg)
        except:
            set_inner_state_a(user, '0')

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
        send_options(bot, user, options, 'Есть ли аккаунт в vk?')
        set_inner_state_a(user, '1')
    elif istate == '1':
        try:
            result = get_options(bot, user, options, msg)

            set_inner_state_a(user, '0')
            
            if result == 'yes':
                set_state_a(user, 'get_vk')
                get_vk(bot, user, msg)    
            else:
                set_state_a(user, 'get_name')
                get_name(bot, user, msg)
        except:
            set_inner_state_a(user, '0')

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
        istate = getattr(user, 'istate')
        print(state + ' << current state')
        print(istate + ' << current state')
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
            'get_specific_type': get_specific_type,
            'get_area': get_area,
            'get_attr_pr': get_attr_pr,
            'get_attr_med': get_attr_med,
            'get_attr_it': get_attr_it,
            'get_attr_pr_2':get_attr_pr_2,
            'get_vacancies': get_vacancies,
            'get_attr_it_2': get_attr_it_2,
            'get_attr_med_2': get_attr_med_2,
            'decline_for': decline_for,
            'get_phone': get_phone,
            'accept': accept,
            'test': test
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



