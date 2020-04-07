from django.contrib import admin
from .models import Category,League,Bet,Outcome,Mybet,Team,GenerateBetcode



class OutcomeInline(admin.TabularInline):
    model = Outcome
    extra = 3

class BetAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team','is_currently_playing','is_available_for_betting')
    fieldsets =  [
                (None, {'fields': ['home_team', 'away_team','is_currently_playing','is_available_for_betting']}),
                ]
    inlines = [OutcomeInline]

# Register your models here.
admin.site.register(Category)
admin.site.register(League)
admin.site.register(Bet,BetAdmin)
admin.site.register(Outcome)
admin.site.register(Mybet)
admin.site.register(Team)
admin.site.register(GenerateBetcode)