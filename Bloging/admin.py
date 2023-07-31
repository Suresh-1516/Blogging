from django.contrib import admin
from .models import *

admin.site.register(Blogpost)
admin.site.register(Like)
admin.site.register(Comment)

