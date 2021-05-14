from django.contrib import admin
from .models import Itinerary, Profile, Rating, User, resetToken

admin.site.register(Profile)
admin.site.register(Itinerary)
admin.site.register(Rating)
admin.site.register(resetToken)



# Register your models here.
