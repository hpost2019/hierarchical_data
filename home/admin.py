from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Structure


admin.site.register(Structure, DraggableMPTTAdmin)
