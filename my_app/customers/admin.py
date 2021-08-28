from django.contrib import admin
from .models import Customers, Professions

class CustomersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'birthdate', 'salary', 'professions')
    list_display_links = ('first_name', 'second_name', 'birthdate', )
    search_fields = ('second_name',)
    list_editable = ('salary',)


class ProfessionsAdmin(admin.ModelAdmin):
    list_display = ('profession_name',)



admin.site.register(Customers, CustomersAdmin)
admin.site.register(Professions)

