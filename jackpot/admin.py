from django.contrib import admin

from . models import Punter, Hexabet, Jackpot, Singlebet

admin.site.register(Hexabet)
admin.site.register(Singlebet)
admin.site.register(Punter)
admin.site.register(Jackpot)
