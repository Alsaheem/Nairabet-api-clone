from django.contrib import admin
from .models import Category,League,Bet,Outcome,Mybet,Team,GenerateBetcode

# Register your models here.
admin.site.register(Category)
admin.site.register(League)
admin.site.register(Bet)
admin.site.register(Outcome)
admin.site.register(Mybet)
admin.site.register(Team)
admin.site.register(GenerateBetcode)