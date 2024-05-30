from django.contrib import admin
from .models import todo
# Register your models here.

class todo_list(admin.ModelAdmin):
    list_display=['id','todo_name','user','user_id']

admin.site.register(todo,todo_list)

# admin.site.register(todo)