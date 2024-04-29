from django.urls import path
from .views import form, submit_form, submission

urlpatterns = [
    path('', form, name='form'),
    path('submit/', submit_form, name='submit_form'),
    path('submission/', submission, name='submission'),
]
