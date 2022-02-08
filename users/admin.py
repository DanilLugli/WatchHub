from django.contrib import admin
from .models import User
from blog.models import Watch, Condition, Maison

# Register your models here.
admin.site.register(Condition)
admin.site.register(Maison)

