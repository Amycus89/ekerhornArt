from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Painting
# Register your models here.

@admin.register(Painting)
class PoemAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget},
    }
