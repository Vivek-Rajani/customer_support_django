from django.contrib import admin
from .models import FormSubmission

class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'message']
    
admin.site.register(FormSubmission, FormSubmissionAdmin)
