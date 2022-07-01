from django.contrib import admin

from mainapp.models import infoofuser
from mainapp.models import equipment,equipment1,requests,requests_apply

# Register your models here.
admin.site.register(infoofuser)
admin.site.register(equipment)
admin.site.register(equipment1)
admin.site.register(requests)
admin.site.register(requests_apply)
