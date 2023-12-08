from django.contrib import admin
from .models import *

# Register article model to admin dashboard
admin.site.register(Article)