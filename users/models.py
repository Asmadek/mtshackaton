from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=500)
    rating = models.IntegerField(null = True, blank=True)

class Area(models.Model):
    name = models.CharField(max_length=128)

class City(models.Model):
    name = models.CharField(max_length=100)

class Person(models.Model):
    """docstring for Person"""
    name = models.CharField(max_length=128)
    date_birth = models.DateField(null=True)
    category = models.IntegerField(null=True, blank=True)

    university = models.ForeignKey(University, null=True)
    vk = models.CharField(max_length=128)

    city = models.ForeignKey(City, null=True)
    phone_number = models.CharField(max_length=15, blank=True)    
    chat_id = models.CharField(max_length=128, blank=True)
    telegram_id = models.CharField(max_length= 128)

    photo_url = models.CharField(max_length = 128)
    
    @property
    def vacancies(self):
        return MarkedVacancy.objects.filter(person=self)

    @property
    def areas(self):
        return MarkedArea.objects.filter(person=self)
   
    @property
    def category_title(self):
        if self.category == 1:
            return "Школьник"
        elif self.category == 2:
            return "Студент"
        else: 
            return "Другое"


    state = models.CharField(max_length=128, blank=True)
    istate = models.CharField(max_length=128, blank=True)



class Vacancy(models.Model):
    area = models.ForeignKey(Area)
    name = models.CharField(max_length=256)
    has_internship = models.BooleanField()


class Test(models.Model):
    area = models.ForeignKey(Area)


class Question(models.Model):
    text = models.CharField(max_length=256)
    test = models.ForeignKey(Test)

class Answer(models.Model):
    queistion = models.ForeignKey(Question)
    text = models.CharField(max_length=256)
    is_right = models.BooleanField()





class Result(models.Model):
    area = models.ForeignKey(Area)
    person = models.ForeignKey(Person)
    score = models.IntegerField()

class MarkedVacancy(models.Model):
    vacancy = models.ForeignKey(Vacancy)
    person = models.ForeignKey(Person)

class MarkedArea(models.Model):
    person = models.ForeignKey(Person)    
    area = models.ForeignKey(Area)
    