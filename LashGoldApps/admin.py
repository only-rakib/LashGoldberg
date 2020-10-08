from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Office_Address,PracticeArea

# Apply summernote to all TextField in model.
class PracticeAreaAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


# Register your models here.
admin.site.register(Office_Address)
admin.site.register(PracticeArea, PracticeAreaAdmin)
