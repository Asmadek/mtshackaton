from django.contrib import admin
from .models import Person, University, Question, Area, City, Test, Answer, Vacancy
# Register your models here.
admin.site.register(Person)
admin.site.register(University)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Area)
admin.site.register(Vacancy)
admin.site.register(City)
