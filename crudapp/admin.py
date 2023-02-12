from django.contrib import admin

from crudapp.models import College,Principle 
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id','cname','clocation','cid','cstate','ccountry'] 

@admin.register(Principle)
class PrincipleAdmin(admin.ModelAdmin):
    list_display=['id','pname','pcity','pid'] 
    
