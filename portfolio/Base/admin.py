from django.contrib import admin
from Base.models import Contact 

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','content','number')

admin.site.register(Contact,ContactAdmin)
